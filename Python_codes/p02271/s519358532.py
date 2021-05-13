def subset_sum(s, a):
	n = len(a)
	dp = [[False for x in range(s+1)] for x in range(n+1)]
	for i in range(n):
		v = a[i]
		for j in range(s+1):
			if v == j:
				dp[i+1][j] = True
			elif v > j:
				dp[i+1][j] = dp[i][j]
			else:
				dp[i+1][j] = dp[i][j] or dp[i][j-v]
	return dp[n][s]

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
for i in range(q):
	if subset_sum(m[i], a) == True:
		print('yes')
	else:
		print('no')
