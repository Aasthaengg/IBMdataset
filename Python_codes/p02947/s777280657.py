# -*- coding: utf-8 -*-
from collections import defaultdict
from scipy.special import comb

n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[''.join(sorted((list(input()))))] += 1

print(sum([comb(i, 2, exact=True) for i in d.values()]))
