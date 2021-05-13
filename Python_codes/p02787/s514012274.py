def main():
	inf=10**9
	h,n=map(int,input().split())
	ab=[]
	r=0
	for i in range(n):
		a,b=map(int,input().split())
		ab.append((a,b))
		r=max(r,a)
	#dp[number][damage]
	dp=[[inf for _ in range(r+h)]for _ in range(n+1)]
	for i in range(n+1):
		dp[i][0]=0
	for i in range(n):
		for j in range(r+h):
			if j-ab[i][0]>=0:
				dp[i+1][j]=dp[i+1][j-ab[i][0]]+ab[i][1]
			dp[i+1][j]=min(dp[i][j],dp[i+1][j])
	ans=inf
	for i in range(r):
		ans=min(ans,dp[n][i+h])
	print(ans)
if __name__ == '__main__':
	main()