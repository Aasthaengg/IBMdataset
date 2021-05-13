MOD = 10**9 + 7

n,m = (int(num) for num in input().split())
s = [int(num) for num in input().split()]
t = [int(num) for num in input().split()]

dp = [[1]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        if s[i-1] == t[j-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] = dp[i][j] % MOD
        
        
print(dp[n][m])
