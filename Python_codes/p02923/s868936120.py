#!/usr/bin/env python3
n, *h = map(int, open(0).read().split())
r = [0] * n
for i in range(1, n):
    if h[i - 1] >= h[i]:
        r[i] = r[i - 1] + 1
    else:
        r[i] = 0
print(max(r))
