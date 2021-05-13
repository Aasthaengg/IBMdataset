def main():
  import sys
  input = sys.stdin.readline
  import numpy as np
  n,k = map(int,input().split())
  s = input()
  chk_0 = []
  chk_1 = []
  c0 = 0
  c1 = 0
  if s[0]=='0':
    c0 += 1
  else:
    c1 += 1
    chk_0.append(0)

  for i in range(n-1):
    if s[i]=='0' and s[i+1]=='0':
      c0 += 1
    if s[i]=='0' and s[i+1]=='1':
      chk_0.append(c0)
      c0 = 0
      c1 = 1
    if s[i]=='1' and s[i+1]=='0':
      chk_1.append(c1)
      c0 = 1
      c1 = 0
    if s[i]=='1' and s[i+1]=='1':
      c1 += 1

  if c0 != 0:
    chk_0.append(c0)
    chk_1.append(0)
  elif c1 != 0:
    chk_1.append(c1)
    chk_0.append(0)

  if len(chk_0) <= k:
    print(n)
    exit()

  ab = np.array([x+y for x,y in zip(chk_0,chk_1)])
  np.cumsum(ab,out=ab)

  ans = ab[k-1]
  for i in range(len(ab)-k):
    chk = ab[k+i]-ab[i]
    chk += chk_1[i]
    ans = max(ans,chk)
  print(ans)
if __name__ == '__main__':
    main()