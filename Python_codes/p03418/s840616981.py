# -*- coding: utf-8 -*-

n, k = map(int, input().split())

cnt = 0
for b in range(1, n + 1):
    q, r = divmod(n + 1, b)
    cnt += q * max(0, b - k) + max(0, r - k)

if k == 0:
    cnt -= n

print(cnt)
