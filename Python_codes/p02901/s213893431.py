n,m=map(int,input().split())
a,c=[],[]
for _ in range(m):
  a.append(list(map(int,input().split()))[0])
  bit=0
  for i in input().split():
    bit|=(1<<(int(i)-1))
  c.append(bit)
inf=float("inf")
dp=[[inf]*(1<<n) for i in range(m+1)]
dp[0][0]=0
for i in range(m):
  for j in range(1<<n):
    dp[i+1][j]=min(dp[i+1][j],dp[i][j])
    next_bit=j|c[i]
    dp[i+1][next_bit]=min(dp[i+1][next_bit],dp[i][j]+a[i])
print(dp[-1][-1] if dp[-1][-1]!=inf else -1)