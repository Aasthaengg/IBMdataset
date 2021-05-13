#!/usr/bin/env python3
import functools
import fractions
n, *a = map(int, open(0).read().split())
gcd = functools.reduce(fractions.gcd, a)
print(gcd)
