#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

for dim in range(1, 4):
    total = 0
    for i in range(n):
        total += abs(x[i]-y[i]) ** dim
    print(round(total ** (1/dim), 6))

maxval = 0
for i in range(n):
    if abs(x[i]-y[i]) > maxval:
        maxval = abs(x[i]-y[i])

print(float(maxval))

