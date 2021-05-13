# -*- coding: utf-8 -*-
N, M = tuple(map(int, input().split()))
coins = sorted(tuple(map(int, input().split())))

counts = [float("inf") for _ in range(N+1)]
counts[0] = 0

for m in range(M):
    coin = coins[m]
    for n in range(coin, N+1):
        counts[n] = min(counts[n], counts[n-coin] + 1)

print(counts[-1])