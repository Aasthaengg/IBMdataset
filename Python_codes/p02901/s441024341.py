n,m=map(int,input().split())
k=[]
for i in range(m):
  a,b=map(int,input().split())
  c=sum(map(lambda x:2**(int(x)-1),input().split()))
  k.append((a,c))

dp=[2**100 for i in range(2**n)]
dp[0]=0
for i in k:
  for j in range(2**n):
    dp[i[1]|j]=min(dp[i[1]|j],dp[j]+i[0])
if dp[-1]==2**100:
  print(-1)
else:
  print(dp[-1])