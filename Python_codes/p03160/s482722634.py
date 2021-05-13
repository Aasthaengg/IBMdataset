n=int(input())
H=list(map(int,input().split()))
INF=float('inf')

dp=[0]*(n+1)
dp[0]=INF
dp[1]=0
for i in range(2,n+1):
  if i-3<0:
    dp[i]=dp[i-1]+abs(H[i-1]-H[i-2])
  else:
    dp[i]=min(dp[i-1]+abs(H[i-1]-H[i-2]),dp[i-2]+abs(H[i-1]-H[i-3]))
    
print(dp[n])