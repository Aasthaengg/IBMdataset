n = int(input())
mod = 10**9 + 7
c = [int(input()) for i in range(n)]

dp = [0 for i in range(n)]
dp[0] = 1
memo = {c[0]:0}
for i in range(1,n):
    if c[i] in memo:
        if memo[c[i]] != i-1:
            dp[i] =(dp[i-1] + dp[memo[c[i]]])%mod
            memo[c[i]] = i
        else:
            dp[i] = dp[i-1]
            memo[c[i]] = i
    else:
        dp[i] = dp[i-1]
        memo[c[i]] = i

print(dp[n-1])