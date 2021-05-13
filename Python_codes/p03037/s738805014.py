#!/usr/bin/env python3
(n, m,), *g = [[*map(int, i.split())] for i in open(0)]
ma = n
mi = 0
for l, r in g:
    mi = max(mi, l)
    ma = min(ma, r)

print(max(ma-mi+1,0))
