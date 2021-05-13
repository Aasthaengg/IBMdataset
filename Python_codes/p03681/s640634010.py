#!/usr/bin/env python3
n, m = map(int, input().split())
mod = 10**9 + 7
if -2 < n - m < 2:
    d = 1
    s = 1
    for i in range(1, n + 1):
        d = d * i % mod
    for i in range(1, m + 1):
        s = s * i % mod
    print((d * s * (1 + (n == m))) % mod)
else:
    print(0)
