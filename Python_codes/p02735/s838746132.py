h,w = map(int,input().split())

s = []
for _ in range(h):
	s.append(list(input()))

inf = float('inf')
dp = [[inf for _ in range(w)] for _ in range(h)]
dp[0][0] = 0

for i in range(h):
	for j in range(w):
		if s[i][j] == ".":
			if j > 0 and i > 0:
				dp[i][j] = min(dp[i-1][j],dp[i][j-1])
			elif j > 0 and i == 0:
				dp[i][j] = dp[i][j-1]
			elif j == 0 and i > 0:
				dp[i][j] = dp[i-1][j]
		else:
			tmp1 = inf
			tmp2 = inf
			if i > 0:
				tmp1 = dp[i-1][j]
				if s[i-1][j] == ".":
					tmp1 += 1
			if j > 0:
				tmp2 = dp[i][j-1]
				if s[i][j-1] == ".":
					tmp2 += 1
			dp[i][j] = min(tmp1,tmp2)
			if i==0 and j==0:
				dp[i][j] = 1

print(dp[h-1][w-1])

