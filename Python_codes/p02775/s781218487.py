N=input()
N='0'+N
M=len(N)
INF=10**12
DP1=[INF]*(M+1)
DP2=[INF]*(M+1)
DP1[0]=0
for i in range(M):
  DP1[i+1]=min(DP1[i]+int(N[i]),DP2[i]+10-int(N[i]))
  DP2[i+1]=min(DP1[i]+int(N[i])+1,DP2[i]+9-int(N[i]))
print(min(DP1[M],DP2[M]+1))