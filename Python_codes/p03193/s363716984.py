#!/usr/bin/env python3

n, h, w = [int(x) for x in input().split()]
c = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    if a >= h and b >= w:
        c += 1
print(c)
