n = int(input())
days_ls = [0] * n
for i in range(n):
    days_ls[i] = list(map(int, input().split()))

dp = [[0]*3 for _ in range(n)]
dp[0] = days_ls[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + days_ls[i][0]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + days_ls[i][1]
    dp[i][2] = max(dp[i-1][1],dp[i-1][0]) + days_ls[i][2]
print(max(dp[-1]))