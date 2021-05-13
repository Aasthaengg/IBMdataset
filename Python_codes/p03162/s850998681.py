n=int(input())
#n,k=map(int, input().split())
a=[[0]*n for _ in range(3)]
for i in range(n):
  a[0][i],a[1][i],a[2][i]=map(int,input().split())
dp=[[0]*n for _ in range(3)]
dp[0][0]=a[0][0]
dp[1][0]=a[1][0]
dp[2][0]=a[2][0]
for i in range(1,n):
  dp[0][i]=max(dp[1][i-1],dp[2][i-1])+a[0][i]
  dp[1][i]=max(dp[0][i-1],dp[2][i-1])+a[1][i]
  dp[2][i]=max(dp[1][i-1],dp[0][i-1])+a[2][i]
print(max(dp[0][-1],dp[1][-1],dp[2][-1]))