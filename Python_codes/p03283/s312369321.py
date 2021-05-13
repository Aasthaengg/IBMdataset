from sys import stdin
from itertools import accumulate
input = stdin.readline
N, M, Q = map(int, input().split())
D = [[0] * (N + 1) for i in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    D[L][R] += 1
for i in range(N - 1, 0, -1):
    for j in range(i, N + 1):
        D[i][j] += D[i + 1][j]
for i in range(1, N + 1):
    D[i] = list(accumulate(D[i]))
for _ in range(Q):
    p, q = map(int, input().split())
    print(D[p][q])