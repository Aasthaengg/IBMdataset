n = int(input())
h = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    if i < n - 2:
        dp[i+2] = min(dp[i+2], dp[i]+abs(h[i] - h[i+2]))
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i] - h[i+1]))
    elif i == n - 2:
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i] - h[i+1]))

print(dp[-1])