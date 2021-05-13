from itertools import product
n = int(input())
mod = 10 ** 9 + 7
dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[0][0][0][0] = 1
# 1:A, 2:G, 3:C, 4:T
for t in range(n):
	for i, j, k, l in product(range(5), repeat=4):
		if not (l == 0 or (j == 1) & (k == 2) & (l == 3) or (i == 1) & (j == 2) & (l == 3) or (j == 1) & (k == 3) & (l == 2)
				  or (j == 2) & (k == 1) & (l == 3) or (i == 1) & (k == 2) & (l == 3)):
			dp[t + 1][j][k][l] += dp[t][i][j][k] % mod
ans = sum(dp[-1][i][j][k] % mod for i, j, k in product(range(1, 5), repeat=3)) % mod
print(ans)