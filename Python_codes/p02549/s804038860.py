N, K = map(int, input().split())
L=[]
R=[]
for i in range(K):
  l,r= map(int, input().split())
  L.append(l)
  R.append(r)

dp=[0]*(N+1)
dp[1]=1
dpd=[0]*(N+2)
dpd[2]=-1

for i in range(1, N):
  for j in range(K):
    dpd[min(i+L[j],N+1)]+=dp[i]
    dpd[min(i+R[j]+1,N+1)]-=dp[i]
  dp[i+1]=(dp[i]+dpd[i+1])%998244353

print(dp[N])