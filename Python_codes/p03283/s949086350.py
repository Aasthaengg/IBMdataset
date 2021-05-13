N, M, Q = map(int, input().split())
C = [[0]*N for _ in range(N)]
for _ in range(M):
    L, R = map(int, input().split())
    C[L-1][R-1] += 1
S = [[0]*(N+1) for _ in range(N+1)]
for r in range(N):
    for l in reversed(range(N)):
        S[l][r] = S[l+1][r] + C[l][r]
D = [[0]*(N+1) for _ in range(N+1)]
for l in range(N):
    for r in range(N):
        D[l][r] = D[l][r-1] + S[l][r]
for _ in range(Q):
    p, q = map(int, input().split())
    print(D[p-1][q-1])
