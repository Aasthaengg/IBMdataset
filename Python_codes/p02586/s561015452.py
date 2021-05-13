r, c, k = map(int, input().split())
dp = [[[0] * (c+1) for _ in range(r+1)] for _ in range(4)]

v_dict = dict()
for _ in range(k):
    y, x, v = map(int, input().split())
    v_dict[(y, x)] = v

for y in range(1, r+1):
    for x in range(1, c+1):
        prev_y_max = 0
        for i in range(4):
            prev_y_max = max(dp[i][y-1][x], prev_y_max)
        dp[0][y][x] = max(prev_y_max, dp[0][y][x-1])
        if (y, x) in v_dict:
            v = v_dict[(y, x)]
            dp[1][y][x] = max(prev_y_max + v, dp[0][y][x-1] + v, dp[1][y][x-1])
            dp[2][y][x] = max(dp[1][y][x-1] + v, dp[2][y][x-1])
            dp[3][y][x] = max(dp[2][y][x-1] + v, dp[3][y][x-1])
        else:
            for i in range(1, 4):
                dp[i][y][x] = dp[i][y][x-1]
ans = 0
for i in range(4):
    ans = max(dp[i][r][c], ans)
print(ans)
