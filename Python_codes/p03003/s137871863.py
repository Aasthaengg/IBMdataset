mod = 1000000007

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]) % mod
        if s[i-1] == t[j-1]: 
            dp[i][j] = (dp[i][j] + dp[i-1][j-1] + 1) % mod
print((dp[n][m]+1) % mod)