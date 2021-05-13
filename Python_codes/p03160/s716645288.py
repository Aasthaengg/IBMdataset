n=int(input())
ab=abs
hr=list(map(int,input().split()))
dp=[-1]*(n+1)
dp[0]=0
dp[1]=ab(hr[1]-hr[0])
for i in range(2,n):
	x=ab(hr[i]-hr[i-2])+dp[i-2]
	y=ab(hr[i]-hr[i-1])+dp[i-1]
	dp[i]=min(x,y)
print(dp[n-1])