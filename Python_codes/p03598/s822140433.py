# -*- coding: utf-8 -*-

N = int(input())
K = int(input())
x = list(map(int, input().split()))

ans = 0
tmp_N = 0
tmp_K = 0
min_xi = 0

for xi in x:
    tmp_N = abs(xi - 0)
    tmp_K = abs(xi - K)
    min_xi = min(tmp_N, tmp_K)
    ans = ans + (min_xi * 2)

print(ans)