s = input()
p = 10 ** 9 + 7
dp = [[0 for _ in range(13)] for j in range(len(s)+1)]
dp[0][0] = 1
for cnt, i in enumerate(reversed(s)):
	if i == "?":
		for f in range(10):
			k = pow(10, cnt, 13)*f%13
			for j in range(13):
				dp[cnt+1][(j+k)%13] = (dp[cnt+1][(j+k)%13] + dp[cnt][j])%p
	else:
		targ = int(i)
		k = pow(10, cnt, 13)*targ%13
		for j in range(13):
			dp[cnt+1][(j+k)%13] = (dp[cnt+1][(j+k)%13] + dp[cnt][j])%p
#print(dp)
print(dp[len(s)][5])