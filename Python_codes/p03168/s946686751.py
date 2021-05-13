n = int(input())
p = list(map(float, input().split()))

# dp[i][j]: 最初のi枚を投げたときに表がj枚となる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[0][0] = 1.0

for i in range(n):
	for j in range(n):
		dp[i + 1][j + 1] += dp[i][j] * p[i] # 表
		dp[i + 1][j] += dp[i][j] * (1 - p[i]) # 裏

res = 0
for j in range(n + 1):
	if n < 2 * j: # 表の枚数 > 裏の枚数
		res += dp[n][j]

print(res)