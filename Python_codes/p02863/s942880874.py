n, t = map(int, input().split())
food = []
for i in range(n):
    food.append(list(map(int, input().split())))

food.sort()

#dp[i][j]: i番目までの料理をいくつか食べて、時間jまでに注文した美味しさの合計のmax
dp = [[0 for i in range(t+1)] for j in range(n+1)]

for i in range(n):
    for j in range(t+1):
        a, b = food[i]
        if j == t:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        elif j + a >= t:
            dp[i+1][t] = max(dp[i][j] + b, dp[i+1][t])
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        else:
            dp[i+1][j+a] = max(dp[i][j] + b, dp[i+1][j+a])
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])

print(dp[n][t])
