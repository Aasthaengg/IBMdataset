#! /usr/bin/env python3

n, m, d = map(int, input().split())

res = 0

if d == 0:
    res = 1
elif n >= 2 * d:
    res = 1 + (n - 2 * d) / n
else:
    res = (n - d) * 2 / n

print(res / n * (m - 1))
