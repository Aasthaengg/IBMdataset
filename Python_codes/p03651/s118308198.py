#!/usr/bin/env python3
from functools import reduce
from math import gcd

n, k, *a = map(int, open(0).read().split())
g = reduce(gcd, a)
if k <= max(a) and k%g <1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
