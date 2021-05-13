import sys
from bisect import bisect_left



N,Q = map(int, input().split())
lines = sys.stdin.readlines()
kkk = []
for line in lines[:N]:
  s, t, x = map(int, line.split())
  kkk.append((x, s, t))
kkk.sort()
ddd = list(map(int, lines[N:]))

ans = [-1] * Q
skip = [-1] * Q
for x, s, t in kkk:
  ss = bisect_left(ddd, s - x)
  tt = bisect_left(ddd, t - x)
  while ss < tt:
    sk = skip[ss]
    if sk == -1:
      ans[ss] = x
      skip[ss] = tt
      ss += 1
    else:
      ss = sk

print('\n'.join(map(str, ans)))
