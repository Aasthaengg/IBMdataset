N, M = (int(i) for i in input().split())
MOD = 10**9 + 7
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

DP = [[0] * (M+1) for counter1 in range(N+1)]
DP[0][0] = 1
for i in range(N):
    DP[i+1][0] = 1
for i in range(M):
    DP[0][i+1] = 1
for i in range(N):
    for j in range(M):
        if S[i] != T[j]:
            DP[i+1][j+1] = DP[i+1][j] + DP[i][j+1] - DP[i][j]
            DP[i+1][j+1] %= MOD
        else:
            DP[i+1][j+1] = DP[i+1][j] + DP[i][j+1]
            DP[i+1][j+1] %= MOD
print(DP[N][M])