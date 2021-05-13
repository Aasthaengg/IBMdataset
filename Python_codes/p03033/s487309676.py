import sys
from bisect import bisect_left



N,Q = map(int, input().split())
STX = [None] * N
for i in range(N):
  s,t,x = map(int, input().split())
  STX[i] = [x,s,t]
STX.sort()
Dn = [None] * (Q+1)
for i in range(Q):
  Dn[i] = int(input())
Dn[Q] = 10**10

ans = [-1] * Q
skip = [-1] * Q
for x, s, t in STX:
  ss = bisect_left(Dn, s - x)
  tt = bisect_left(Dn, t - x)
  while ss < tt:
    sk = skip[ss]
    if sk == -1:
      ans[ss] = x
      skip[ss] = tt
      ss += 1
    else:
      ss = sk

print('\n'.join(map(str, ans)))
