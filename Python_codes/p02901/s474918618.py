n,m=map(int,input().split())
a=[None]*m
b=[None]*m
c=[None]*m
for i in range(m):
  a[i],b[i]=map(int,input().split())
  c[i]=list(map(int,input().split()))
INF=10**18
dp=[INF for _ in  range(1<<n)]
dp[(1<<n)-1]=0
for bit in range((1<<n)-2,-1,-1):
  for u in range(m):
    dumy=bit
    flag=0
    for i in c[u]:
      i-=1
      if not ((bit>>i) & 1):
        dumy|=(1<<i)
        flag=1
    if flag:
      dp[bit]=min(dp[bit],dp[dumy]+a[u])
print([dp[0],-1][dp[0]==INF])