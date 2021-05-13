#all you can eat

N, T = map(int, input().split())
food = [tuple(map(int, input().split())) for i in range(N)]

dp = [[0]*(3010) for i in range(3010)]

for i in range(N):
    time, value = food[i]
    for j in range(T):
        if j >= time:
            dp[i+1][j] = max(dp[i][j], dp[i][j-time] + value)
        else:
            dp[i+1][j] = dp[i][j]
        dp[i][j] = max(dp[i][j], dp[i][j-1])

rev_dp = [[0]*(3010) for i in range(3010)]
food.reverse()

for i in range(N):
    time, value = food[i]
    for j in range(T):
        if j >= time:
            rev_dp[i+1][j] = max(rev_dp[i][j], rev_dp[i][j-time] + value)
        else:
            rev_dp[i+1][j] = rev_dp[i][j]
    dp[i][j] = max(dp[i][j], dp[i][j-1])


ans = 0
for x in range(N):
    ans = max(ans, max(dp[N-1-x][t] + rev_dp[x][T-1-t]
                       for t in range(T))+food[x][1])
print(ans)

