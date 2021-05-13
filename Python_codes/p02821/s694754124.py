def main():
  import bisect
  import sys
  from itertools import accumulate
  input = sys.stdin.readline
  def hsnum(x):
    num = 0
    for i in a:
      y = x-i
      num += n-bisect.bisect_left(a,y)
    return num
  n,m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort()
  suma = [0]+list(accumulate(a))
  lx = 0
  rx = 2*10**5+2
  error = 0
  while lx+1 < rx:
    mx = (lx+rx)//2
    if hsnum(mx) < m:
      rx = mx
    elif hsnum(mx) > m:
      lx = mx + 1
    else:
      lx = mx
      break
  if hsnum(lx)<m:
    lx -= 1
  error = hsnum(lx)-m
  ans = 0
  for i in a:
    rema = lx - i
    j = bisect.bisect_left(a,rema)
    ans += (n-j)*i-suma[j]
  ans += suma[n]*n
  print(ans-error*lx)
if __name__ == "__main__":
    main()