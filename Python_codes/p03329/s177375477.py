N = int(input())

dp = [0]*(10**5+1)
for i in range(1, 10**5+1):
	dp[i] = dp[i-1]+1
	cnt = 0
	while 6**cnt<=i:
		dp[i] = min(dp[i], dp[i-6**cnt]+1)
		cnt += 1
	cnt = 0
	while 9**cnt<=i:
		dp[i] = min(dp[i], dp[i-9**cnt]+1)
		cnt += 1
print(dp[N])