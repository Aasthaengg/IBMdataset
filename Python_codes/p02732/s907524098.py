#!/usr/bin/env python3
from collections import Counter

from scipy.special import comb

_, *a = map(int, open(0).read().split())
c = Counter(a)
s = sum(comb(i, 2, exact=True) for i in c.values())
for i in a:
    print(s - c[i] + 1)
