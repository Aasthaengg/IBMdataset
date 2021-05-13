n = int(raw_input())
dp = [+float('inf')] * (n+1)
dp[0] = 0
for i in range(1, n+1):
	q = 1
	if i - q >= 0:
		dp[i] = min(dp[i], 1 + dp[i - q])
	for u in [6,9]:
		p = 1
		q = u ** p
		while((i  - q) >= 0):
			dp[i] = min(dp[i], 1 + dp[i - q])
			p += 1
			q = u ** p
print dp[n]
