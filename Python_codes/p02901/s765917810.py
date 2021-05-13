n,m=map(int,input().split())
keys=[None]*m
INF = 10**10
dp=[INF]*(2**n)
dp[0]=0
for i in range(m):
  a,b=map(int,input().split())
  c=list(map(int,input().split()))
  cond=0
  for j in c:
    cond+=2**(j-1)
  keys[i]=[a,cond]
for key in keys:
  for sta in range(2**n):
        dp[sta|key[1]]=min(dp[sta|key[1]],dp[sta]+key[0])
print(dp[-1] if dp[-1] != INF else -1)
