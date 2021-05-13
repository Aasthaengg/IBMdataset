N, C = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(N)]

cum_col = [0 for _ in range(N+1)]
for i in range(N):
    cum_col[i+1] = cum_col[i] + sushi[i][1]

clockwise_dp = [None for _ in range(N)]
clockwise_best = [0, 0]
anti_clockwise_dp = [None for _ in range(N)]
anti_clockwise_best = [0, 0]
for i in range(N):
    if clockwise_best[0] < cum_col[i+1] - sushi[i][0]:
        clockwise_best = [cum_col[i+1]-sushi[i][0], sushi[i][0]]
    clockwise_dp[i] = clockwise_best

for i in range(N-1, -1, -1):
    if anti_clockwise_best[0] < cum_col[N] - cum_col[i] - C + sushi[i][0]:
        anti_clockwise_best = [
            cum_col[N]-cum_col[i]-C+sushi[i][0],
            C-sushi[i][0]
        ]
    anti_clockwise_dp[i] = anti_clockwise_best

ans = max(clockwise_dp[N-1][0], anti_clockwise_dp[0][0])
for i in range(N-1):
    ans = max(ans,
              clockwise_dp[i][0],
              anti_clockwise_dp[i+1][0],
              clockwise_dp[i][0]+anti_clockwise_dp[i+1][0]-min(clockwise_dp[i][1], anti_clockwise_dp[i+1][1])
              )

print(ans)
