import bisect
a,b,q = map(int,input().split())
s = [-10**11]+[int(input()) for _ in range(a)]+[10**11]
t = [-10**11]+[int(input()) for _ in range(b)]+[10**11]
for i in range(q):
  ans = 10**11
  x = int(input())
  l = bisect.bisect(s,x)
  m = bisect.bisect(t,x)
  arr = [[s[l-1],s[l]],[t[m-1],t[m]]]
  for i in range(4):
    S = 0
    now = x
    for j in range(2):
      t0 = now-arr[j][i >> j & 1]
      S += t0*((-1)**(t0<0))
      now -= t0
    if ans > S:
      ans = S
  for i in range(4):
    S = 0
    now = x
    for j in range(2):
      t0 = now-arr[1-j][i >> j & 1]
      S += t0*((-1)**(t0<0))
      now -= t0
    if ans > S:
      ans = S
  print(ans)