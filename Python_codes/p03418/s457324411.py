# -*- coding: utf-8 -*-

n, k = map(int, input().split())

if k == 0:
    print(n * n)
    exit()

cnt = 0
for b in range(k + 1, n + 1):
    q, r = divmod(n - k + 1, b)
    cnt += (b - k) * q + min((b - k), r)

print(cnt)
