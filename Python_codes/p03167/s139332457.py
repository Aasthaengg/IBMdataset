arr=[] 
n,m=map(int,input().split()) 
dp=[[0 for j in range(m)] for i in range(n)] 
for i in range(n):
	arr.append(input()) 
dp[0][0]=1 
for i in range(1,n):
	if arr[i][0]!='#':
		dp[i][0]+=dp[i-1][0]
	else:
		break  
for i in range(1,m):
	if arr[0][i]!='#':
		dp[0][i]+=dp[0][i-1]
	else:
		break 


for i in range(1,n):
	for j in range(1,m):
		if arr[i][j]!='#':
			dp[i][j]=dp[i-1][j]+dp[i][j-1]  
mod=10**9+7 
print(dp[-1][-1]%mod)