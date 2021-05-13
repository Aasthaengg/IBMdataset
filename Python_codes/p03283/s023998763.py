import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
A = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    A[0][R] += 1
    A[0][N] -= 1
    A[L+1][R] -= 1
    A[L+1][N] += 1

for i in range(N+1):
    for j in range(N):
        A[i][j+1] += A[i][j]

for i in range(N):
    for j in range(N+1):
        A[i+1][j] += A[i][j]

for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    print(A[p][q])