N=int(input())
A=[]
for i in range(2):
  a=list(map(int,input().split()))
  A.append(a)

dp=[[0 for i in range(N)] for j in range(2)]

dp[0][0]=A[0][0]
dp[1][0] = A[0][0]+A[1][0]
for i in range(1,N):
  dp[0][i]=dp[0][i-1]+A[0][i]
  dp[1][i]=A[1][i]+max(dp[1][i-1],dp[0][i])

print(dp[1][N-1])