#!/usr/bin/env python3
from scipy.special import comb

n, *s = open(0).read().split()
d = {}
for i in s:
    l = "".join(sorted(j for j in i))
    if l in d:
        d[l] += 1
    else:
        d[l] = 1
print(sum(comb(i, 2,exact=True) for i in d.values()))
