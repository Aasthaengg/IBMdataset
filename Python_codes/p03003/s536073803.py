def main():
	N, M = map(int, input().split())
	S = list(map(int, input().split()))
	T = list(map(int, input().split()))
	S.append(0)
	T.append(0)
	MOD = 10**9+7

	dp0 = [[0 for _ in range(M+2)] for _ in range(N+2)]
	dp1 = [[0 for _ in range(M+2)] for _ in range(N+2)]
	dp0[0][0] = 1
	for i in range(N+1):
		for j in range(M+1):
			dp0[i+1][j] += dp0[i][j]
			dp0[i+1][j] %= MOD
			dp1[i][j] += dp0[i][j]
			dp1[i][j] %= MOD
			dp1[i][j+1] += dp1[i][j]
			dp1[i][j+1] %= MOD

			if S[i] == T[j]:
				dp0[i+1][j+1] += dp1[i][j]
				dp0[i+1][j+1] %= MOD
	print(dp1[N][M])


if __name__ == '__main__':
	main()