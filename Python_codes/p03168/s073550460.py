n=int(input())
l=input().split()
li=[float(i) for i in l]
#dp[i][j] denotes out of first i tosses get j heads
dp=[[0 for i in range(n+1)] for j in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
	dp[i][0]=dp[i-1][0]*(1-li[i-1])
for j in range(1,n+1):
	dp[0][j]=0
for i in range(1,n+1):
	for j in range(1,i+1):
		dp[i][j]=(dp[i-1][j-1]*li[i-1])+dp[i-1][j]*(1-li[i-1])
prob=0
for j in range(n+1):
	if(j>n/2):
		prob+=dp[n][j]
print(prob)
