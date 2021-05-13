#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
s = sum(a)
ans = 10**18
c = 0
for i in range(n - 1):
    c += a[i]
    ans = min(ans, abs(2 * c - s))
print(ans)
