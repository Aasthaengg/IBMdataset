#!/usr/bin/env python3
from collections import defaultdict

(n, ), *p = [[*map(int, i.split())] for i in open(0)]
d = defaultdict(int)
for i in range(n):
    for j in range(n):
        if i != j:
            d[(p[i][0] - p[j][0], p[i][1] - p[j][1])] += 1
print(n*(n<2) or n - max(d.values()))
