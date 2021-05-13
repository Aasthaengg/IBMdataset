import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60

N, M, Q = map(int, readline().split())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = map(int, readline().split())
    G[l - 1][r - 1] += 1

csum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        csum[i + 1][j + 1] = csum[i + 1][j] + csum[i][j + 1] - csum[i][j] + G[i][j]

ans = []
for _ in range(Q):
    p, q = map(int, readline().split())
    ans.append(csum[q][q] - csum[q][p - 1] - csum[p - 1][q] + csum[p - 1][p - 1])

print(*ans, sep='\n')
