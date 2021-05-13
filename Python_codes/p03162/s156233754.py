n = int(input())

vals = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = vals[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + vals[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + vals[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + vals[i][2]

print(max(dp[n-1]))