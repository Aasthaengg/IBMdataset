def smaller(x, y):
	if x < y: return x
	return y

N, M = map(int, input().split())
coins = list(map(int, input().split()))
dp = []
for i in range(0, N+1):
	dp.append(100000)
dp[0] = 0
for i in range(0, N):
	for j in range(0, M):
		if i+coins[j] <= N:
			dp[i+coins[j]] = smaller(dp[i]+1, dp[i+coins[j]])
print(dp[N])
