import numpy as np

h, w = map(int,input().split())
s = [input() for _ in range(h)]

dp = np.zeros((h, w), dtype = np.int64)
dp[0][0] = 1
mod = 10**9 + 7

for i in range(h):
	for j in range(w):
		if s[i][j] == ".":
			if j == 0:
				if i == 0:
					continue
				dp[i][j] = dp[i-1][j]
			else:
				if i == 0:
					dp[i][j] = dp[i][j-1]
				else:
					dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod
print(dp[h-1][w-1])