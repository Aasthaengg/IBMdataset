MOD = 10**9 + 7
N = int(input())
stones = [int(input()) for _ in range(N)]
dp = [0] * (N+1)
rightmost = [0] * (2 * 10**5 + 1)
dp[0] = 1
for i, c in enumerate(stones):
    dp[i+1] += dp[i]
    dp[i+1] %= MOD
    if rightmost[c] not in [0, i]:
        dp[i+1] += dp[rightmost[c]]
        dp[i+1] %= MOD
    rightmost[c] = i+1
print(dp[N])