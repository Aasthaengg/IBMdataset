
def rec(i, w):
	if dp[i][w] != -1:
		return dp[i][w]

	if i == 0:
		if w == 0:
			return True
		else:
			return False

	res = 0
	if w >= a[i - 1] and rec(i - 1, w - a[i - 1]) == 1:
		res = 1
	
	if rec(i - 1, w) == 1:
		res = 1

	dp[i][w] = res
	return dp[i][w]

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

dp = [[-1] * (2000 + 1) for _ in range(n + 1)]

for i in range(m):
	print('yes') if rec(n, q[i]) == 1 else print('no')
