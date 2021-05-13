n = int(input())
mod = 10**9+7

s = [0 for _ in range(2*10**5)]
pos = [-1 for _ in range(2*10**5)]
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[-1] = 1

for i in range(n):
	x = int(input())
	if i == 0:
		dp[0] = 1
	else:
		p = pos[x - 1]
		if p == i - 1:
			dp[i] = dp[i - 1]
		elif p > -1:
			dp[i] = dp[i - 1] + dp[p]
			dp[i] %= mod
		else:
			dp[i] = dp[i - 1]
	pos[x - 1] = i
print(dp[n - 1])
