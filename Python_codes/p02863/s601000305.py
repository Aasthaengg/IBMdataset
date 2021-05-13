n, t = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(n)]

MAX = 10000
dish.sort()
dp = [[0] * MAX for _ in range(n+1)]

for i in range(n):
    time, value = dish[i]
    for j in range(t):
        dp[i+1][j+time] = max(dp[i+1][j+time], dp[i][j] + value)
    for j in range(MAX):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(max(dp[n]))