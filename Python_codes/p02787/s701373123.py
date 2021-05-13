h,n=map(int,input().split())

damage=[]
cost=[]
for i in range(n):
  a,b=map(int,input().split())
  damage.append(a)
  cost.append(b)

  
dp=[[float('inf')]*(h+1) for i in range(n+1)]
dp[0][0]=0

for i in range(n):
  for j in range(h+1):
    dp[i+1][j]=min(dp[i+1][j],dp[i][j])
    dp[i+1][min(j+damage[i],h)]=min(dp[i+1][min(j+damage[i],h)],dp[i+1][j]+cost[i])


print(dp[-1][-1])