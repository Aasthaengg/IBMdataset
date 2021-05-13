#!/usr/bin/env python3
from bisect import bisect_right

n, *L = map(int, open(0).read().split())
L.sort()
ans = 0
c = [0] * (2 * 10**3 + 1)
for i in range(2 * 10**3 + 1):
    c[i] = bisect_right(L, i)
for i in range(n):
    for j in range(i + 1, n):
        ans += c[L[i] + L[j] - 1] - c[L[j] - L[i]] - 1 - (L[j] - L[i]*2 < 0)
print(ans//3)
