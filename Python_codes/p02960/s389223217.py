from sys import stdin
s = stdin.readline()[:-1]

length = len(s)

dp = [[0 for i in range(13)]for j in range(100100)]

s = list(reversed(s))

dp[0][0]=1
ten = 1
mod = 1000000007


for i in range(length):
	if s[i] == '?':
		for num in range(10):
			d = num*ten
			for j in range(13):
				k = (j+d)%13
				dp[i+1][k] += dp[i][j]
				dp[i+1][k] %= mod
	else:
		num = int(s[i])
		d = num*ten
		for j in range(13):
			k = (j+d)%13
			dp[i+1][k] += dp[i][j]
			dp[i+1][k] %= mod
	ten *= 10
	ten %= 13

print(int(dp[length][5]%mod))