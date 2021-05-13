#!/usr/bin/env python3
from math import gcd

a, b, c = map(int, input().split())
print("YNEOS"[c % gcd(a, b) > 0::2])
