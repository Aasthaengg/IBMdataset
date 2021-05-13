n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1000)
dp[0] = 1000

for i in range(1, n):
    for j in range(i):
        stock = dp[j] // a[j] * a[i] + dp[j] % a[j]
        dp[i] = max(dp[i - 1], stock)
print(dp[n-1])