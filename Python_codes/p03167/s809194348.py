h,w=map(int,input().split())
m,mod=[],10**9+7
for i in range(h):m.append(input())
dp=[[0]*w for i in range(h)]
dp[0][0]=1
for i in range(h):
	for j in range(w):
		if m[i][j]=='.':
			if i==0 and j!=0:dp[i][j]=dp[i][j-1]
			elif i!=0 and j==0:dp[i][j]=dp[i-1][j]
			elif i!=0 and j!=0:dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
print(dp[h-1][w-1])