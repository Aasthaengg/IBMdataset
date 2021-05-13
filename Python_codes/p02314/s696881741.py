N, M = map(int, input().split())
C = [0] + list(map(int, input().split()))
C.sort()

dp = [[0] * (N+1) for _ in range(M+1)]
for i in range(N+1):
	dp[1][i] = i
for i in range(2,M+1):
	for j in range(1, N+1):
		if C[i] > j:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = min(dp[i-1][j], dp[i][j-C[i]]+1)

print(dp[M][N])
