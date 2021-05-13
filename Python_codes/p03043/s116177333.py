#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N, K = map(int, input().split())
res = 0
for i in range(1, N + 1):
    p = 1
    x = i
    while x < K:
        x *= 2
        p /= 2
    res += p
res /= N
print(res)
