#!/usr/bin/env python3
import math

n = int(input())
x = {}

for i in range(1, 50001):
    x.setdefault(math.floor(i * 1.08), i)


try:
    print(x[n])
except:
    print(":(")
