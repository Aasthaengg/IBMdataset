N = int(input())
a = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = -10**18

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0]+a[i-1], dp[i-1][1]-a[i-1])
    dp[i][1] = max(dp[i-1][0]-a[i-1], dp[i-1][1]+a[i-1])
print(dp[N][0])

