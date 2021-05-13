n=int(input())
A=list(map(int,input().split()))
INF=float('inf')

dp=[[0 for _ in range(n)] for _ in range(2)]
dp[0][0]=A[0]
dp[1][0]=-INF
for i in range(1,n):
  dp[0][i]=max(dp[0][i-1],dp[1][i-1])+A[i]
  dp[1][i]=max(dp[0][i-1]-2*A[i-1]-A[i],dp[1][i-1]+2*A[i-1]-A[i])

print(max(dp[0][n-1],dp[1][n-1]))