#!/usr/bin/env python3
a, b, c, k = map(int, input().split())
if abs(a - b) > 10**18:
    print("Unfair")
else:
    print((a - b) * (-1)**k)
