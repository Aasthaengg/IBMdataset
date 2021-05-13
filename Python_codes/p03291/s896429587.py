#初期化
m = (10 ** 9) + 7
S = list(input())
N = len(S)
dp = [[0 for i in range(N + 2)] for j in range(3)]
three = [0 for i in range(10 ** 5 + 1)]
three[0] = 1
for i in range(1, 10 ** 5 + 1):
	three[i] = (three[i - 1] * 3) % m

#DP
que = 0
for i in range(N):
	if S[i] == "A":
		dp[0][i + 1] = dp[0][i] + three[que]
		dp[1][i + 1] = dp[1][i]
		dp[2][i + 1] = dp[2][i]
	elif S[i] == "B":
		dp[0][i + 1] = dp[0][i]
		dp[1][i + 1] = dp[0][i] + dp[1][i]
		dp[2][i + 1] = dp[2][i]
	elif S[i] == "C":
		dp[0][i + 1] = dp[0][i]
		dp[1][i + 1] = dp[1][i]
		dp[2][i + 1] = dp[1][i] + dp[2][i]
	else:
		dp[0][i + 1] = 3 * dp[0][i] + three[que]
		dp[1][i + 1] = 3 * dp[1][i] + dp[0][i]
		dp[2][i + 1] = 3 * dp[2][i] + dp[1][i]
		que += 1
	dp[0][i + 1], dp[1][i + 1], dp[2][i + 1] = dp[0][i + 1] % m, dp[1][i + 1] % m, dp[2][i + 1] % m

print(dp[2][N])