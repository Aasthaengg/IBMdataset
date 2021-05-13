import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 9)
INF = 1 << 60

N, M, Q = map(int, input().split())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    G[l - 1][r - 1] += 1

csum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        csum[i + 1][j + 1] = csum[i + 1][j] + csum[i][j + 1] - csum[i][j] + G[i][j]

ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    ans.append(csum[q][q] - csum[q][p - 1] - csum[p - 1][q] + csum[p - 1][p - 1])

print(*ans, sep='\n')
