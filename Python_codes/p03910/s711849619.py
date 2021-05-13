#!/usr/bin/env python3
from math import ceil

n = int(input())
a = ceil(((1 + 8 * n)**0.5 - 1) / 2)
for i in range(a):
    if a * (a + 1) // 2 - n - 1 != i:
        print(i + 1)
