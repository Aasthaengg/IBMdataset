#!/usr/bin/env python3
n, k, s = map(int, input().split())
ans = [s] * k + [10**9 - (s == 10**9)] * (n - k)
print(*ans)
