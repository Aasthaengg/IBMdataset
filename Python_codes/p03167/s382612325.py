
def solve(H, W, grid):
	MOD = 10 ** 9 + 7
	dp = [0] * (W)
	for j in range(W):
		if grid[0][j] == '#':
			break
		if j == 0:
			dp[j] = 1
		else:
			dp[j] = dp[j-1]

	for i in range(1, H):
		dp2 = [0] * W
		dp2[0] = dp[0] if grid[i][0] != '#' else 0
		for j in range(1, W):
			dp2[j] = dp[j] + dp2[j-1] if grid[i][j] != '#' else 0
		dp = dp2

	return dp[-1] % MOD

H, W = [int(s) for s in input().split()]
grid = []
for _ in range(H):
	grid.append([s for s in input()])
print(solve(H, W, grid))