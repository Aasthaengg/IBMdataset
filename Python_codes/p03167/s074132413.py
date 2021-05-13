l=input().split()
r=int(l[0])
c=int(l[1])
l=[]
for i in range(r):
	s=input()
	l.append(s)
dp=[[0 for i in range(c)]for i in range(r)]
dp[0][0]=1
for i in range(1,r):
	if(l[i][0]=='#'):
		dp[i][0]=0
		continue
	dp[i][0]=dp[i-1][0]
for j in range(1,c):
	if(l[0][j]=='#'):
		dp[0][j]=0
		continue
	dp[0][j]=dp[0][j-1]
for i in range(1,r):
	for j in range(1,c):
		if(l[i][j]=='#'):
			dp[i][j]=0
		else:
			dp[i][j]=dp[i-1][j]+dp[i][j-1]
			dp[i][j]%=1000000007
print(dp[r-1][c-1])
