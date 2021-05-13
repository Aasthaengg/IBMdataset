#!/usr/bin/env python3
from functools import reduce
from math import gcd

n, *t = map(int, open(0).read().split())
t.sort()
print(reduce(lambda a, b: a * b // gcd(a, b), t))
