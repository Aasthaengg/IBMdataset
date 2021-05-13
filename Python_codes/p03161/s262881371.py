n, k = map(int, input().split())

arr = list(map(int, input().split()))

dp = [float('inf')]*n

dp[0] = 0
dp[1] = abs(arr[0]-arr[1])

for i in range(2, n):
    for j in range(i-1, max(-1, i-k-1), -1):
        dp[i] = min(dp[i], dp[j]+abs(arr[i]-arr[j]))

print(dp[-1])
