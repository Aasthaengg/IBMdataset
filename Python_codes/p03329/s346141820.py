N = int(input())

dp = [i for i in range(N+1)]

for i in range(1,N+1):
    dp[i] = min(dp[i], 1+dp[i-1])
    tmp = 1
    while tmp <= i:
        dp[i] = min(dp[i], 1+dp[i-tmp])
        tmp *= 6
    tmp = 1
    while tmp <= i:
        dp[i] = min(dp[i], 1+dp[i-tmp])
        tmp *= 9

print(dp[-1])
