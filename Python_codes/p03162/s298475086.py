n = int(input())
x = [0] * n
#x = [[0]*3 for i in range(n)]

for i in range(0, n):
    x[i] = list(map(int, input().split()))

dp = [[0]*3 for i in range(n)]

for i in range(0, 3):
    dp[0][i] = x[0][i]

for i in range(0, n-1):
    dp[i+1][0] = max(dp[i][1], dp[i][2]) + x[i+1][0]
    dp[i+1][1] = max(dp[i][2], dp[i][0]) + x[i+1][1]
    dp[i+1][2] = max(dp[i][0], dp[i][1]) + x[i+1][2]

ans = 0
for i in range(0, 3):
    ans = max(ans, dp[n-1][i])

print(ans)
