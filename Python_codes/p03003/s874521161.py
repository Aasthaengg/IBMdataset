N, M = map(int, input().split())
MOD = 10**9 + 7
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0 for i in range(M+1)] for j in range(N+1)]
for j in range(M):
    dp[1][j + 1] = dp[1][j] + 1 if s[0] == t[j] else dp[1][j]

for i in range(N):
    dp[i + 1][1] = dp[i][1] + 1 if t[0] == s[i] else dp[i][1]

for i in range(1, N):
    for j in range(1, M):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] + 1)%MOD
        else:
            dp[i + 1][j + 1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j])%MOD
    
print((dp[N][M] + 1)%MOD)
