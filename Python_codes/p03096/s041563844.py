N=int(input())
C=[int(input())-1 for i in range(N)]
mod=10**9+7
pre_dp=[0]*(max(C)+1)
dp=[0]*(N+1)
dp[0]=1
dp[1]=1
pre_dp[C[0]]=1
for i in range(1,N):
  if C[i]!=C[i-1]:
    dp[i+1]=(dp[i]+pre_dp[C[i]])%mod
    pre_dp[C[i]]=(pre_dp[C[i]]+dp[i])%mod
  else:
    dp[i+1]=dp[i]
    
print(dp[N])
