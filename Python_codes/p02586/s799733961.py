import sys

R, C, K = map(int, sys.stdin.readline().split())

grid = [[0 for _ in range(C+1)] for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, sys.stdin.readline().split())
    grid[r][c] = v

# r行目、c列目にいるときに、その行でアイテムをi個取得している場合の最大価値
dp0 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp1 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp2 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp3 = [[0 for _ in range(C+1)] for _ in range(R+1)]
# print(dp)
for r in range(1, R+1):
    for c in range(1, C+1):
        # 取らない
        dp0[r][c] = max((dp0[r][c-1], dp0[r-1][c], dp1[r-1][c], dp2[r-1][c], dp3[r-1][c]))
        dp1[r][c] = max(dp1[r][c-1], dp1[r][c])
        dp2[r][c] = max(dp2[r][c-1], dp2[r][c])
        dp3[r][c] = max(dp3[r][c-1], dp3[r][c])

        # 取る
        dp1[r][c] = max(dp0[r-1][c] + grid[r][c], dp1[r][c])
        dp1[r][c] = max(dp1[r-1][c] + grid[r][c], dp1[r][c])
        dp1[r][c] = max(dp2[r-1][c] + grid[r][c], dp1[r][c])
        dp1[r][c] = max(dp3[r-1][c] + grid[r][c], dp1[r][c])

        dp1[r][c] = max(dp0[r][c-1] + grid[r][c], dp1[r][c])
        dp2[r][c] = max(dp1[r][c-1] + grid[r][c], dp2[r][c])
        dp3[r][c] = max(dp2[r][c-1] + grid[r][c], dp3[r][c])


# print(dp0)
# print(dp1)
# print(dp2)
# print(dp3)
print(max((dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C])))