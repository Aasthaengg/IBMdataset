N=int(input())
A=[]
for i in range(2):
  a=list(map(int,input().split()))
  A.append(a)

dp=[[0 for i in range(N)] for j in range(2)]

dp[0][0]=A[0][0]
for i in range(1,N):
  dp[0][i]=dp[0][i-1]+A[0][i]

dp[1][0] = A[0][0]+A[1][0]
for j in range(1,N):
  dp[1][j]=A[1][j]+max(dp[1][j-1],dp[0][j])

print(dp[1][N-1])