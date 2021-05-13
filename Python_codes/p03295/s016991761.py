# -*- coding: utf-8 -*-
N, M = map(int, input().split())
items = [list(map(int, input().split())) for i in range(M)]
items = sorted(items, key=lambda x: x[1])
last = 0
res = 0
for a, b in items:
    if last <= a:
        res += 1
        last = b
print(res)
