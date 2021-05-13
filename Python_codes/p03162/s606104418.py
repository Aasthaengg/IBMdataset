n=int(input())
a=[]
b=[]
c=[]

for _ in range(n):
	tmp=list(map(int,input().split()))
	a.append(tmp[0])
	b.append(tmp[1])
	c.append(tmp[2])
dp=[[0 for j in range(n)]for i in range(3)]
dp[0][0]=a[0]
dp[1][0]=b[0]
dp[2][0]=c[0]
for i in range(1,n):
	dp[0][i]=a[i]+max(dp[1][i-1],dp[2][i-1])
	dp[1][i]=b[i]+max(dp[2][i-1],dp[0][i-1])
	dp[2][i]=c[i]+max(dp[0][i-1],dp[1][i-1])
print(max(dp[0][n-1],dp[1][n-1],dp[2][n-1]))
