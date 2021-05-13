N,M= map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
mod=10**9+7
ans=[[0 for e in range(M)] for f in range(N)]
rui=[[0 for e in range(M)] for f in range(N)]
for j in range(M):
 if j!=0:
  rui[0][j]=rui[0][j-1]
 if S[0]==T[j]:
  ans[0][j]=1
  rui[0][j]+=ans[0][j]
for i in range(1,N):
 rui[i][0]=rui[i-1][0]
 if S[i]==T[0]:
  ans[i][0]=1
  rui[i][0]+=ans[i][0]
for i in range(1,N):
 for j in range(1,M):
  rui[i][j]=rui[i][j-1]+rui[i-1][j]-rui[i-1][j-1]
  if S[i]==T[j]:
   ans[i][j]=(rui[i-1][j-1]+1)
   rui[i][j]+=ans[i][j]
  rui[i][j]%=mod
print((rui[N-1][M-1]+1)%mod)