n=int(input())
l=list(map(int,input().split()))
dp=l.copy()
for i in range(n-1):

	dp1=dp.copy()
	l=list(map(int,input().split()))
	for j in range(3):
		ans=float('-inf')
		for k in range(3):
			if(j!=k):
				ans=max(ans,l[j]+dp[k])
		dp1[j]=ans
	dp=dp1.copy()
print(max(dp))
