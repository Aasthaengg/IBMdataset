from sys import stdout, stdin, maxsize

n, k = map(int, stdin.readline().split())
ls = list(map(int, stdin.readline().split()))
dp = [maxsize] * (n + 1)
dp[1] = 0
if n == 1:
	print(0)
else:
	dp[2] = abs(ls[1] - ls[0])
	for i in range(3, n + 1):
		j = 1
		while j <= k and i - j >= 0:
			dp[i] = min(dp[i - j] + abs(ls[i - 1] - ls[i - 1 - j]), dp[i])
			j += 1
	print(dp[n])
