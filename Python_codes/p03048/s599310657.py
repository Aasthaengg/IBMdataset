r, g, b, n = map(int, input().split())
ball = [0, r, g, b]
dp = [[0] * 4 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for k in range(4):
        if k == 0:
            if i != 0:
                dp[i][k] = 0
        else:
            if i - ball[k] < 0:
                dp[i][k] = dp[i][k-1]
            else:
                dp[i][k] = dp[i-ball[k]][k] + dp[i][k-1]

print(dp[n][3])