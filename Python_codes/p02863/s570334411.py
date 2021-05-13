N, T = map(int, input().split())


AB_array = [list(map(int, input().split())) for _ in range(N)]

AB_array = sorted(AB_array, key=lambda x: x[0])

dp = [[0] * T for _ in range(N)]

ans = 0

for i in range(1, N):
    for j in range(T):
        if j >= AB_array[i - 1][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1]
                           [j - AB_array[i - 1][0]] + AB_array[i - 1][1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ans = max(ans, dp[i - 1][-1] + AB_array[i - 1][1])
ans = max(ans, dp[-1][-1] + AB_array[-1][1])
print(ans)
