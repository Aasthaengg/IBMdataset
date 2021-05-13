# -*- coding: utf-8 -*-

n, k = map(int, input().split())

proba = 0.0

for i in range(1, n+1):
    exp = 0

    while i*(2**exp) < k:
        exp+=1

    proba += (1/n) * (0.5**exp)

print(proba)
