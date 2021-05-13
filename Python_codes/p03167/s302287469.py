h,w=map(int,input().split())
dp=[ [-1]*(w+1) for _ in range(h+1) ]
for i in range(h):
  i+=1
  tmp=input()
  for j in range(w):
    j+=1
    if tmp[j-1]=='.':
      dp[i][j]=0
    else:
      dp[i][j]=-1
dp[1][1]=1

for i in range(1,h+1):
  for j in range(1,w+1):
    if i==1 and j==1:continue
    if dp[i][j]==-1:continue
    dp[i][j]=0
    if dp[i-1][j]!=-1:
      dp[i][j]+=dp[i-1][j]
    if dp[i][j-1]!=-1:
      dp[i][j]+=dp[i][j-1]
    dp[i][j]=dp[i][j]%(10**9+7)
#print(dp)
print(dp[-1][-1])