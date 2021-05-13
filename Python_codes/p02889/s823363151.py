import math
import sys
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))

T = []
T1 = []
for _ in range(N):
    T.append([float("inf")] * N)
    T1.append([float("inf")] * N)
for n in range(N):
    T[n][n] = 0
    T1[n][n] = 0

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    A -= 1
    B -= 1
    T[A][B] = C
    T[B][A] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            if T[i][j] > T[i][k] + T[k][j]:
                T[i][j] = T[i][k] + T[k][j]

for j in range(N):
    for i in range(N):
        if i == j:
            continue
        if T[j][i] <= L:
            T1[j][i] = 1
            T1[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if T1[i][j] > T1[i][k] + T1[k][j]:
                T1[i][j] = T1[i][k] + T1[k][j]

Q = int(input())
for _ in range(Q):
    S, G = list(map(int, input().split()))
    if math.isinf(T1[S-1][G-1]):
        print(-1)
    else:
        print(T1[S-1][G-1]-1)
