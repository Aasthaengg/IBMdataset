#!/usr/bin/env python3
from math import gcd
a, b, c, d = map(int, input().split())


def dev(n):
    return b // n - -(-a // n) + 1

print(dev(1) - dev(c) - dev(d) + dev(c * d//gcd(c,d)))
