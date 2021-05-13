#!/usr/bin/env python3
n, k, *P = map(int, open(0).read().split())
p = [(i + 1) / 2 for i in P]
c = sum(p[:k])
ans = c
for i in range(n - k):
    c = c + p[i + k] - p[i]
    ans = max(c, ans)
print(ans)
