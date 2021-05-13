N, K = map(int, input().split())
L = list(map(int, input().split()))
dp = [-1 for k in range(K+1)]
dp[0] = 1
def fn(n):
	if dp[n] != -1:
		return dp[n]
	for i in L:
		if n >= i:
			if fn(n-i) == 1:
				dp[n] = 0
				return 0
	dp[n] = 1
	return 1
for l in range(1, 	K):
	fn(l)
if fn(K) == 0:
	print("First")
else:
	print("Second")
