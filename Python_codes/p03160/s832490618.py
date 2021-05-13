from sys import stdout, stdin

n = int(stdin.readline())
ls = list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
if n == 1:
	print(0)
elif n == 2:
	print(abs(ls[1] - ls[0]))
else:
	dp[2] = abs(ls[1] - ls[0])
	for i in range(3, n+1):
		dp[i] = min(dp[i - 1] + abs(ls[i - 1] - ls[i - 2]), dp[i - 2] + abs(ls[i - 1] - ls[i - 3]))
	print(dp[n])
