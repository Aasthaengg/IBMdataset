#!/usr/bin/env python3
L, R = map(int, input().split())
l = L % 2019
r = R % 2019
if R - L < 2019 and r > l:
    print(
        min(i * j % 2019 for i in range(l, r + 1)
            for j in range(i + 1, r + 1)))
else:
    print(0)
