MOD = 10**9+7
n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = 1
cum = [[0 for _ in range(m+1)] for _ in range(n+1)]
cum[0][0] = 1
for i in range(1, n+1):
	cum[i][0] = 1
for j in range(1, m+1):
	cum[0][j] = 1

for i in range(1, n+1):
	for j in range(1, m+1):
		if s[i-1] == t[j-1]:
			dp[i][j] = cum[i-1][j-1]
			dp[i][j] %= MOD
		cum[i][j] = cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1] + dp[i][j]
		cum[i][j] %= MOD

print(cum[n][m])