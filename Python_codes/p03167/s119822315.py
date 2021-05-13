h,w=map(int,input().split())
li=[]
mod=10**9+7
for i in range(h):
  li.append(input())
dp=[[0 for i in range(w)] for j in range(h)]
for i in range(h):
  if(li[i][0]=="#"):
      break
  dp[i][0]=1
for j in range(w):
    if(li[0][j]=="#"):
        break
    dp[0][j]=1
for i in range(1,h):
  for j in range(1,w):
    if li[i][j]==".":
      dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
print(dp[h-1][w-1]%mod) 