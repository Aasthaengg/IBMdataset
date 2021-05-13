MOD = 1000000007

N,M = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

dp = [[0 for j in range(M+1)] for i in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
for j in range(M+1):
    dp[0][j] = 1

for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]
        else:
            dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]-dp[i][j]
        dp[i+1][j+1] %= MOD

print(dp[-1][-1])