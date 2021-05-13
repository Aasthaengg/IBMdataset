N=int(input())

h=list(map(int,input().split()))

#初期化
dp=[float('inf') for i in range(N)]
dp[0]=0

#DP
for i in range(N-1):
  if dp[i+1] > dp[i]+abs(h[i+1]-h[i]):
    dp[i+1]=dp[i]+abs(h[i+1]-h[i])
  if i!= N-2:
    if dp[i+2] > dp[i]+abs(h[i+2]-h[i]):
      dp[i+2]=dp[i]+abs(h[i+2]-h[i])
      
print(dp[N-1])