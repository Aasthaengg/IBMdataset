#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
ans = 0
for i in range(0, n, 2):
    ans += a[i] % 2 == 1
print(ans)
