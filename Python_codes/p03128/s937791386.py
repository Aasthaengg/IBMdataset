def main():  
  import sys
  read = sys.stdin.buffer.read
  readline = sys.stdin.buffer.readline
  readlines = sys.stdin.buffer.readlines

  n,m = map(int,readline().split())
  a = list(map(int,readline().split()))
  d5 = False
  d9 = False

  if 5 in a:
    d5 = True
  if 9 in a:
    d9 = True
  chk = set()
  for i in a:
    if d5 and (i == 2 or i == 3):
      continue
    if d9 and i == 6:
      continue
    chk.add(i)

  dp = [-float('inf')]*(n+1)
  dp[0] = 0
  f = [0,2,5,5,4,5,6,3,7,6]

  for i in range(2,n+1):
    for j in chk:
      F = f[j]
      if F <= i:
        dp[i] = max(dp[i-F]*10+j,dp[i])

  print(dp[n])

if __name__ == '__main__':
    main()
