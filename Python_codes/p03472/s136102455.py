#!/usr/bin/env python3
import bisect
import math

n, h = map(int, input().split())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
max_a = max(a)
b.sort()
idx = bisect.bisect_right(b, max_a)
ans = 0
tmp = 0
for i in range(n - 1, -1, -1):
    tmp += b[i]
    if tmp >= h:
        print(n - i)
        exit()
    if i <= idx:
        break

print(n - idx + math.ceil((h - sum(b[idx:])) / max_a))
