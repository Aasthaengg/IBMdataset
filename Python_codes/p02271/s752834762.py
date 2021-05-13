def subset_sum(n, s, a):
	dp = [[0 for x in range(s+1)] for x in range(n+1)]
	for i in range(n):
		v = a[i]
		for j in range(s+1):
			if v==j or (v<j and dp[i][j-v]>0):
				dp[i+1][j] = dp[i][j] + 1
			else:
				dp[i+1][j] = dp[i][j]
	return dp[n][s] > 0

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
for i in range(q):
	if subset_sum(n, m[i], a) == True:
		print('yes')
	else:
		print('no')

