N=int(input())
hcost=list(map(int,input().split()))
dp=[0]*(N+1)
dp[1]=abs(hcost[1]-hcost[0])

for i in range(2,N):
  dp[i]=min(dp[i-2]+abs(hcost[i-2]-hcost[i]),dp[i-1]+abs(hcost[i-1]-hcost[i]))
  
print(dp[N-1])
