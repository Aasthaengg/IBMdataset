#!/usr/bin/env python3
from functools import reduce
from math import gcd

n, *a = map(int, open(0).read().split())
print(reduce(gcd, a))
