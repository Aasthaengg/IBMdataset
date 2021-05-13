#!/usr/bin/env python3
N, M = map(int, input().split())
S = [[*map(int, input().split())] for _ in range(N)]
C = [[*map(int, input().split())] for _ in range(M)]
for a, b in S:
    mi = 10**9
    ans = 51
    for i in range(M):
        c, d = C[i]
        if abs(a - c) + abs(b - d) < mi:
            ans = i + 1
            mi = abs(a - c) + abs(b - d)
    print(ans)
