h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

MOD = 10 ** 9 + 7
dp = [[0] * w for _ in range(h)]

i = 0
while i < w and grid[0][i] != '#':
	dp[0][i] = 1
	i += 1

j = 0
while j < h and grid[j][0] != '#':
	dp[j][0] = 1
	j += 1

for i in range(1, h):
	for j in range(1, w):
		if grid[i][j] == '#':
			dp[i][j] == 0
		else:
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
			dp[i][j] %= MOD

print(dp[h-1][w-1])
