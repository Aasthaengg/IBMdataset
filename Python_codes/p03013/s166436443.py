MOD = 10**9 + 7
N, M = map(int,input().split())
a = [int(input()) for k in range(M)]
dp = [0]*(N+2)
dp[0] = 1
for e in a:
    dp[e] = -1
for k in range(N):
    if dp[k] != -1:
        if dp[k+1] != -1:
            dp[k+1] += dp[k]
            dp[k+1] %= MOD
        if dp[k+2] != -1:
            dp[k+2] += dp[k]
            dp[k+2] %= MOD
print(max(0,dp[N]))
