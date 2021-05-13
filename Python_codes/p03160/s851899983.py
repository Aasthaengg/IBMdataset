n = int(input())
arr = list(map(int, input().strip().split()))

dp = [float('inf') for i in range(n)]
dp[0] = 0

for i in range(n-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(arr[i]-arr[i+1]))
    if i < n-2:
        dp[i+2] = min(dp[i+2], dp[i] + abs(arr[i]-arr[i+2]))

print(dp[-1])
