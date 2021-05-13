if __name__ == '__main__':
	n, m = map(int, input().split())
	coin_list = list(map(int, input().split()))
	dp = [50000] * (n + 1)
	dp[0] = 0

	for coin in coin_list:
		for i in range(n - coin + 1):
			if dp[i + coin] > dp[i] + 1:
				dp[i + coin] = dp[i] + 1

	print(dp[-1])
