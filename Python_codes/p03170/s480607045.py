def solve(ls, k):
	dp = [False for i in range(k + 1)]
	for i in range(k + 1):
		for stone in ls:
			if stone <= i and not dp[i - stone]:
				dp[i] = True
	return dp[k]


n, k = map(int, input().split())
ls = list(map(int, input().split()))
if solve(ls, k):
	print('First')
else:
	print('Second')
