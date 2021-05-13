n,m=map(int,input().split())
a=[0]*m
b=[0]*m
c=[[] for i in range(m)]
for i in range(m):
  a[i],b[i] =map(int,input().split())
  c[i] = sum([2**(int(x)-1) for x in input().split()])
# N
dp = [1000000000 for i in range(2**n)]
dp[0]=0
for i in range(2**n):
  for j in range(m):
    dp[i|c[j]] = min(dp[i|c[j]], dp[i]+a[j])
if dp[2**n-1]==1000000000:
  print(-1)
else:
  print(dp[2**n-1])
