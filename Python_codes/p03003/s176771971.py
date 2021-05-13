N, M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

dp = [[0 for i in range(M+1)] for j in range(N+1)]
SUM = [[0 for i in range(M+1)] for j in range(N+1)]
mod = 10 ** 9 + 7

for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i+1][j+1] = SUM[i][j] + 1
        else:
            dp[i+1][j+1] = 0
        SUM[i+1][j+1] = SUM[i][j+1] + SUM[i+1][j] - SUM[i][j] + dp[i+1][j+1]
        dp[i+1][j+1] %= mod
        SUM[i+1][j+1] %= mod

print((SUM[N][M] + 1) % mod)