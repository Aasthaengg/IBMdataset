n = int(input())
h = list(map(int, input().split()))

dp = [10**18] * n
dp[0] = 0
for i in range(n-1):
    if i == n-2:
        dp[i+1] = min(dp[i] + abs(h[i+1] - h[i]), dp[i+1])
    else:
        dp[i+1] = min(dp[i] + abs(h[i+1] - h[i]), dp[i+1])
        dp[i+2] = min(dp[i] + abs(h[i+2] - h[i]), dp[i+2])
        
print(dp[-1])