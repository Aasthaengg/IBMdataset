n, a, b = map(int,input().split())
x = list(map(int,input().split()))
dp = [10**9]*(n+1)
dp[0] = 0
for i in range(n - 1):
    dp[i + 1] = min(dp[i] + a*(x[i + 1]-x[i]), dp[i] + b)
print(dp[n-1])