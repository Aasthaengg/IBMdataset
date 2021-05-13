#!/usr/bin/env python
from bisect import *

n, m = map(int, input().split())
p = [0 for _ in range(m)]
y = [0 for _ in range(m)]
for i in range(m):
    p[i], y[i] = map(int, input().split())

d = [[] for _ in range(n)]
for i in range(m):
    d[p[i]-1].append(y[i])

for i in range(len(d)):
    d[i] = sorted(d[i])

ls = rs = ''
def complement(nstr):
    while len(nstr) != 6:
        nstr = '0' + nstr
    return nstr

for i in range(m):
    ls = complement(str(p[i]))
    r = bisect_right(d[p[i]-1], y[i])
    rs = complement(str(r))
    ans = ls+rs
    print(ans)
