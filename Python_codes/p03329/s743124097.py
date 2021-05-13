n = int(input())

dp = [n+1]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    j = 1
    while j <= n:
        dp[i] = min(dp[i], dp[i-j]+1)
        j *= 6

    k = 1
    while k <= n:
        dp[i] = min(dp[i], dp[i-k]+1)
        k *= 9

print(dp[n])
