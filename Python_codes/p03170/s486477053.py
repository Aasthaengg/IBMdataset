N, K = map(int, input().split())
L = list(map(int, input().split()))
dp = [-1 for k in range(K+1)]
# dp[0] = 1
def fn(n):
	if dp[n] != -1:
		return dp[n]
	if n == 0:
		dp[n] = 0
		return dp[n]
	ans = 0
	for i in L:
		if n >= i:
			if fn(n-i) == 0:
				ans = 1
				break
	dp[n] = ans		
	return dp[n]
for l in range(K):
	fn(l)
if fn(K) == 1:
	print("First")
else:
	print("Second")