N=int(input())
mod=10**9+7
DP=[[0]*256 for i in range(N+2)]
NO=[False]*256
S='AGCT'
T=0
for a in range(4):
  for b in range(4):
    for c in range(4):
      for d in range(4):
        T=list(S[a]+S[b]+S[c]+S[d])
        NO[a*64+b*16+c*4+d]=('AGC' in ''.join(T))
        for l in range(3):
          T[l],T[l+1]=T[l+1],T[l]
          NO[a*64+b*16+c*4+d]|=('AGC' in ''.join(T))
          T[l],T[l+1]=T[l+1],T[l]
DP[0][-1]=1
for i in range(N+1):
  for j in range(256):
    if NO[j]:
      DP[i][j]=0
      continue
    for k in range(4):
      DP[i+1][(j*4+k)&255]=(DP[i+1][(j*4+k)&255]+DP[i][j])%mod
P=0
for i in range(256):
  P+=DP[N][i]
print(P%mod)