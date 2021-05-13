#!/usr/bin/env python3

N = int(input())

F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = float("inf") * -1

for i in range(1, 2 ** 10):
    idx = []
    times = []
    for j in range(10):
        if i >> j & 1 == 1:
            idx.append(j)
    for f in F:
        total = 0
        for i in idx:
            if f[i]:
                total += 1
        times.append(total)
    bft = 0
    for p, t in zip(P, times):
        bft += p[t]
    ans = max(bft, ans)

print(ans)