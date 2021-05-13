#!/usr/bin/env python3
from math import degrees, atan

a, b, x = map(int, input().split())
bot = a * a * b
if x * 2 > bot:
    print(degrees(atan((bot - x) * 2 / a**3)))
else:
    print(degrees(atan(b**2 * a / (2 * x))))
