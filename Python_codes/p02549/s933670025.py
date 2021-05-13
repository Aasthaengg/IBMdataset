N, K = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(K)]

dp = [0] * (N + 1)
dp_sums = [0] * (N + 1)
dp[1] = dp_sums[1] = 1

for i in range(2,N+1):
    for l, r in S: 
        if i >= r + 1:
            dp[i] += dp_sums[i - l] - dp_sums[i - r - 1] 
            dp_sums[i] = dp_sums[i-1] + dp[i]
        elif i > l and i < r + 1:
            dp[i] += dp_sums[i - l] 
            dp_sums[i] = dp_sums[i-1] + dp[i]
        elif i <= l:
            dp_sums[i] = dp_sums[i-1] + dp[i]
    dp[i] %= 998244353
    dp_sums[i] %= 998244353
print(dp[N])