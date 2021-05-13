N, M, Q = map(int, input().split())

S = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    S[l][r] += 1

C = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        C[i][j] = C[i-1][j] + C[i][j-1] + S[i][j] - C[i-1][j-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(C[r][r] - C[r][l-1] - C[l-1][r] + C[l-1][l-1])

