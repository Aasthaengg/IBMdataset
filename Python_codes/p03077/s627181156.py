#!/usr/bin/env python3
from math import ceil
n, a, b, c, d, e = map(int, open(0).read().split())
s = min(a, b, c, d, e)
print(4 + ceil(n/s))
