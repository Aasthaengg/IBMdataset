N,M=map(int,input().split())
mod=10**9+7
S=[int(i) for i in input().split()]
T=[int(i) for i in input().split()]
dp=[[0]*(M+1) for i in range(N+1)]
dp[0][0]=1
Sum=[[0]*(M+1) for i in range(N+1)]
for i in range(N+1):
  Sum[i][0]=1
for j in range(M+1):
  Sum[0][j]=1
for i in range(N):
  for j in range(M):
    if S[i]==T[j]:
      dp[i+1][j+1]=Sum[i][j]
    Sum[i+1][j+1]=(dp[i+1][j+1]+Sum[i][j+1]+Sum[i+1][j]-Sum[i][j])%mod
print(Sum[N][M]) 
#print(dp)
#print(Sum)