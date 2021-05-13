N,T=map(int,input().split())
A=[]
for i in range(N):
  a,b=map(int,input().split())
  A.append((a,b))
A=sorted(A)
dp=[[0]*(T) for j in range(N)]
#print(A)

for i in range(N):
  for j in range(T):
    if j>=A[i][0]:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-A[i][0]]+A[i][1])
    else:
      dp[i][j]=dp[i-1][j]
#print(dp)
bma=[0]
t=0
for i in range(N-1,0,-1):
  t=max(t,A[i][1])
  bma=[t]+bma
#print(bma)
ans=0
for i in range(N):
  d=dp[i][-1]+bma[i]
  ans=max(d,ans)
print(ans)