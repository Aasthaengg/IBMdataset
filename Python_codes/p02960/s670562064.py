S=input()
N=len(S)
mod=10**9+7
DP=[[0]*13 for i in range(N+1)]
DP[0][0]=1
for i in range(N):
  if S[i]=='?':
    for j in range(13):
      for k in range(10):
        DP[i+1][(j*10+k)%13]+=DP[i][j]
    for j in range(13):
      DP[i+1][j]%=mod
  else:
    for j in range(13):
      DP[i+1][(j*10+int(S[i]))%13]=DP[i][j]
print(DP[N][5])