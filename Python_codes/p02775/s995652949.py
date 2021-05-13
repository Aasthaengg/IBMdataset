s = map(int,list(raw_input()))
dp = [[0,0] for _ in range(len(s))]
for i in range(len(dp)):
	a = (dp[i - 1][0] if i - 1 >= 0 else 0) + s[i]
	b = (dp[i - 1][1] if i - 1 >= 0 else 1) + 10 - s[i]
	dp[i][0] = min(a,b)

	a = (dp[i - 1][0] if i - 1 >= 0 else 0) + s[i] + 1
	b = (dp[i - 1][1] if i - 1 >= 0 else 1) + 10 - s[i] - 1
	dp[i][1] = min(a,b)
print dp[-1][0]



