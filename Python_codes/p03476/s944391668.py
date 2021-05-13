INF=10**5+1
p=[1]*INF
for i in range(2,INF):
  if p[i]:
    for j in range(2*i,INF,i):p[j]=0
p[0],p[1]=0,0
dp=[0]*INF
for i in range(1,INF,2):
  if p[i]*p[(i+1)//2]:dp[i]=1
for i in range(1,INF):
  dp[i]+=dp[i-1]
q=int(input())
for i in range(q):
  l,r=map(int,input().split())
  print(dp[r+1]-dp[l-1])