H,N=map(int,input().split())
AB=[]
for i in range(N):
  AB.append(list(map(int,input().split())))
dp=[10**8]*(H+1)
dp[0]=0
i=0

for i in range(H+1):
  for A,B in AB:
    if i-A>=0:
      dp[i]=min(dp[i-A]+B,dp[i])
  for A,B in AB:
    if i+A>H:
      dp[-1]=min(dp[-1],dp[i]+B)
print(dp[-1])
