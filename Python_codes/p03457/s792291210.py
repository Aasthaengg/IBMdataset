#!/usr/bin/env python3
import math
n = int(input())
txy = [map(int, input().split()) for _ in range(n)]
t, x, y = [list(i) for i in zip(*txy)]

gt = 0
gx = 0
gy = 0

for i in range(n):
    wt = t[i] -gt
    ww = abs(x[i] - gx) + abs(y[i] - gy)
    if (wt < ww) or ((wt - ww) % 2 == 1):
        print("No")
        break

    gt = t[i]
    gx = x[i]
    gy = y[i]

else:
    print("Yes")