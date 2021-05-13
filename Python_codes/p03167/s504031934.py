mod=1000000007
n,m=map(int,input().split())
ll=[]
dp=[]
for i in range(n):
  s=input()
  ll.append(s)
  l=[0]*m
  dp.append(l)
for i in range(n):
  if(ll[i][0]=='#'):
    break
  dp[i][0]=1
for j in range(m):
  if(ll[0][j]=='#'):
    break
  dp[0][j]=1
for i in range(1,n):
  for j in range(1,m):
    if(ll[i][j]!='#'):
    	dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
print(dp[n-1][m-1])