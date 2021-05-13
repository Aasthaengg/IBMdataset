S = int(input())
mod = 10**9 + 7
dp = [0]*(S+1)
dp[0] = 1
for k in range(S-2):
    for l in range(k+3,S+1):
        dp[l] += dp[k]
        dp[l] %= mod
print(dp[S])
