n,k=map(int,input().split())
ab=abs
k=min(n,k)
hr=list(map(int,input().split()))
dp=[-1]*(n+1)
dp[0]=0
dp[1]=ab(hr[1]-hr[0])
for i in range(1,k):
	x=ab(hr[i]-hr[i-1])+dp[i-1]
	for j in range(1,i+1):
		y=ab(hr[i]-hr[i-j])+dp[i-j]
		x=min(x,y)
	dp[i]=x




for i in range(k,n):
	x=ab(hr[i]-hr[i-1])+dp[i-1]
	h=hr[i]
	for j in range(1,k+1):
		y=ab(h-hr[i-j])+dp[i-j]
		x=min(x,y)
	
	dp[i]=x
print(dp[n-1])