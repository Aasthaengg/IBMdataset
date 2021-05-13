N,K=map(int,input().split())
A=list(map(int,input().split()))
dp=[0]*(2*(10**5)+1)
for i in range(N):
  dp[A[i]]+=1
dp.sort(reverse=True)
bns=sum(dp[K:])
print(bns)