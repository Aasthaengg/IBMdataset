# -*- coding: utf-8 -*-

N, X = map(int, input().split())
min_m = 1000
ans = 0

for i in range(N):
    mi = int(input())
    min_m = min(min_m, mi)
    X -= mi
    ans += 1

ans += X // min_m

print(ans)