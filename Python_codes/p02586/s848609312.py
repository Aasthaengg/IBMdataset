R, C, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]

items = [[0] * (C + 1) for _ in range(R + 1)]
for r, c, v in X:
    items[r][c] = v

dp0 = [[0] * (C + 1) for _ in range(R + 1)]
dp1 = [[0] * (C + 1) for _ in range(R + 1)]
dp2 = [[0] * (C + 1) for _ in range(R + 1)]
dp3 = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        dp0[i][j] = max(dp0[i - 1][j], dp1[i - 1][j], dp2[i - 1][j], dp3[i - 1][j])

        dp3[i][j] = max(dp3[i][j], dp3[i][j - 1])
        dp2[i][j] = max(dp2[i][j], dp2[i][j - 1])
        dp1[i][j] = max(dp1[i][j], dp1[i][j - 1])
        dp0[i][j] = max(dp0[i][j], dp0[i][j - 1])

        if items[i][j]:
            dp3[i][j] = max(dp3[i][j], dp2[i][j] + items[i][j])
            dp2[i][j] = max(dp2[i][j], dp1[i][j] + items[i][j])
            dp1[i][j] = max(dp1[i][j], dp0[i][j] + items[i][j])

print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))
