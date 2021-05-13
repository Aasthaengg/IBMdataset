# -*- coding: utf-8 -*-
from bisect import bisect_left
from sys import stdin



readl = stdin.readline

## input
N,Q = map(int, readl().rstrip().split())
STX = [list(map(int, readl().rstrip().split())) for _ in range(N)]
Dn = [None for _ in range(Q+1)]
for i in range(Q):
  Dn[i] = int(readl().rstrip())
Dn[Q] = 10**10
ans = [-1] * (Q+1)
skip = [-1] * (Q+1)

for s,t,x in sorted(STX,key=lambda x:x[2]):
  l = bisect_left(Dn,s-x)
  r = bisect_left(Dn,t-x)
  while l < r:
    if skip[l] < 0:
      ans[l] = x
      skip[l] = r
      l += 1
    else:
      l = skip[l]

for d in ans[:-1]:
  print(d)