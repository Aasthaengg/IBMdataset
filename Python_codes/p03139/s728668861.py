#!/usr/bin/env python3

n, a, b = [int(x) for x in input().split()]
ma = a if a <= b else b
mi = 0 if n >= a + b else a + b - n
print(ma, mi)
