x=int(input())
data=[100,101,102,103,104,105]
dp=[0]*(x+1)
dp[0]=1
for i in data:
  for j in range(i,x+1):
    if dp[j-i]==1:
      dp[j]=1
print(dp[x])