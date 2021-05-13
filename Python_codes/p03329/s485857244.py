n = int(raw_input())
dp = [j for j in range(n+1)] 
for i in range(1, n+1):
	for u in [6,9]:
		p = 1
		q = u ** p
		while((i  - q) >= 0):
			dp[i] = min(dp[i], 1 + dp[i - q])
			p += 1
			q = u ** p
print dp[n]
