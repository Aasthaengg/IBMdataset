N,M=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
X=[[0]*(M+1) for i in range(N+1)]
DP=[[0]*M for i in range(N)]
DP[0][0]=0
mod=10**9+7
for i in range(N):
  for j in range(M):
    if S[i]==T[j]:
      DP[i][j]=(X[i][j]+1)%mod
    X[i+1][j+1]=(DP[i][j]+X[i+1][j]+X[i][j+1]-X[i][j])%mod
print((X[N][M]+1)%mod)