#!/usr/bin/env python3
import sys
from fractions import gcd

for line in sys.stdin:
    [a, b] = [int(x) for x in line.split()]
    print(int(gcd(a, b)), int(a / gcd(a, b) * b))