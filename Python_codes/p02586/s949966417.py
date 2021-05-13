R, C, K = map(int, input().split())
values = [[0] * C for i in range(R)]
for i in range(K):
	r, c, v = map(int, input().split())
	values[r - 1][c - 1] = v

dp = [[[0] * C for i in range(R)] for j in range(4)]

dp[1][0][0] = values[0][0]

for i in range(R):
	for j in range(C):
		if values[i][j] == 0:
			if j != 0:
				for k in range(4):
					dp[k][i][j] = max(dp[k][i][j], dp[k][i][j - 1])
			if i != 0:
				for k in range(4):
					dp[0][i][j] = max(dp[0][i][j], dp[k][i - 1][j])
		else:
			#取る
			if j != 0:
				for k in range(1, 4):
					dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i][j - 1] + values[i][j])
			if i != 0:
				for k in range(4):
					dp[1][i][j] = max(dp[1][i][j], dp[k][i - 1][j] + values[i][j])
			#取らん
			if j != 0:
				for k in range(4):
					dp[k][i][j] = max(dp[k][i][j], dp[k][i][j - 1])
			if i != 0:
				for k in range(4):
					dp[0][i][j] = max(dp[0][i][j], dp[k][i - 1][j])

ans = 0
for k in range(4):
	ans = max(ans, dp[k][-1][-1])
print(ans)