N,T=map(int,input().split())

ablist=[]
bsum=0
for _ in range(N):
  a,b=map(int,input().split())
  ablist.append((a,b))
  bsum+=b
ablist.sort()
  
dp=[[0]*T for _ in range(N+1)]
for i in range(1,N+1):
  a,b=ablist[i-1]
  for j in range(T):
    dp[i][j]=dp[i-1][j]
    if j-a>=0:
      dp[i][j]=max(dp[i][j],dp[i-1][j-a]+b)      
#print(dp[N])

if dp[N][T-1]==bsum:
  print(bsum)
else:
  answer=0
  for i in range(1,N+1):
    answer=max(answer,dp[i-1][T-1]+ablist[i-1][1])
  print(answer)