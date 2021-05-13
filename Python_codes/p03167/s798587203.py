h, w = map(int, input().split())
field = [input() for _ in range(h)]
MOD = 10 ** 9 + 7

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1

for i in range(1, w):
    if field[0][i] == ".":
        dp[0][i] = dp[0][i-1] 

for i in range(1, h):
    if field[i][0] == ".":
        dp[i][0] = dp[i-1][0]

for row in range(1, h):
    for col in range(1, w):
        if field[row][col] == ".":
            dp[row][col] = (dp[row-1][col] + dp[row][col-1]) % MOD
print(dp[-1][-1])

