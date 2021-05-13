N=int(input())
MOD=10**9+7
DP1=[0 for _ in range(N+3)]
DP2=[0 for _ in range(N+3)]
DP1[3]=1
DP2[3]=1
for i in range(4,N+1):
  DP1[i]=(DP2[i-3]+1)%MOD
  DP2[i]=(DP1[i]+DP2[i-1])%MOD
print(DP1[N])