S = int(input())
mod = 10**9+7

dp = [0] * (S+1)
dp[0] = 1
if S >=3:
    for n in range(3, S+1):
        dp[n] = (dp[n-1] + dp[n-3]) % mod

print(dp[S] % mod)
