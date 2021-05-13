n, m = map(int, input().split())
mod = 10**9+7
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
seta = set([int(input()) for _ in range(m)])

for i in range(2, n+1):
    if not i-1 in seta:
        dp[i] += dp[i-1]
    if not i-2 in seta:
        dp[i] += dp[i-2]
    dp[i] %= mod

print(dp[-1])
