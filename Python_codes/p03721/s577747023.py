N,K=map(int,input().split())
dp=[0]*(10**5)
ans=0
for _ in range(N):
  a,b=map(int,input().split())
  dp[a-1]+=b
for j in range(len(dp)):
  if K<=ans+dp[j]:
    print(j+1)
    exit()
  ans+=dp[j]