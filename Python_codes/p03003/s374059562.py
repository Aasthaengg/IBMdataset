MOD = 10**9 + 7
N, M = map(int, input().split())
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

dp = [[0 for j in range(2010)] for i in range(2010)]
dp[0][0] = 1
for s in range(N+1):
    for t in range(M+1):
        if 0 < s and 0 < t and S[s-1] == T[t-1]:
            dp[s][t] += dp[s-1][t-1]
        if 0 < s:
            dp[s][t] += dp[s-1][t]
        if 0 < t:
            dp[s][t] += dp[s][t-1]
        if 0 < s and 0 < t:
            dp[s][t] -= dp[s-1][t-1]
        dp[s][t] %= MOD
print(dp[N][M])
