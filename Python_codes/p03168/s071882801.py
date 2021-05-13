n=int(input())
h=list(map(float,input().split()))
dp=[[0 for j in range(i+3)] for i in range(n)]

dp[0][0]=1-h[0]
dp[0][1]=h[0]
for i in range(1,n):
	for j in range(i+2):
		dp[i][j]=dp[i-1][j-1]*h[i]+dp[i-1][j]*(1-h[i])
sum=0
for i in range(n//2+1,n+1):
	sum=sum+dp[n-1][i]
print(sum)