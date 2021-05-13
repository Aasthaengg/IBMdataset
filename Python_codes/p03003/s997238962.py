n,m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
PR = 1000000007

dp = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(n+1):
	dp[i][0] = 1

for j in range(m+1):
	dp[0][j] = 1 

for i in range(n):
	for j in range(m):
		#aa
		sumI = 0
		sumI = dp[i+1][j]
#		for jj in range(0,j):
#			if s[i] == t[jj]:
#				sumI=(sumI + dp[i][jj]) % PR
		
		sumJ = 0
		sumJ = dp[i][j+1]
#		for ii in range(0,i):
#			if t[j] == s[ii]:
#				sumJ=(sumJ + dp[ii][j]) % PR
		
		if s[i] == t[j]:
			dp[i+1][j+1] = (sumI + sumJ) % PR
		else:
			dp[i+1][j+1] = (sumI + sumJ - dp[i][j]) % PR
#		print("i: %d j: %d  sumI: %d sumJ:%d dp[i][j]:%d" % (i+1,j+1,sumI,sumJ,dp[i+1][j+1]))

#print(dp)
print(dp[n][m])
