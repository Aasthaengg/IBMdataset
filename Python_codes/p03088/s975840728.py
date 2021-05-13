def summ(M):
    S = 0
    for i in range(4):
        for j in range(4):
            S += M[i][j]
            S %= MOD
    return S

N = int(input())
MOD = 10**9 + 7
D = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+3)]
for i in range(4):
    for j in range(4):
        D[1][i][j][3] = 1
for n in range(2,N):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                D[n][i][j][k] = sum(D[n-1][j][k])%MOD
    for l in range(4):
        D[n][2][1][l] -= D[n-1][1][l][0]
        D[n][2][l][1] -= D[n-1][l][1][0]
    D[n][2][1][1] += D[n-1][1][1][0]
    D[n][1][2][0] = 0
    D[n][2][0][1] = 0
    D[n][2][1][0] = 0
print(sum(summ(D[N-1][i]) for i in range(4))%MOD)