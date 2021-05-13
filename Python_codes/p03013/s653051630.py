n,m=map(int,input().split())
dp=[1]*n 
for i in range(m):
    dp[int(input())-1]=0
if n==1:
  if m==1:
    print(0)
  else:
    print(1)
else:
  if dp[1]==1:
    dp[1]=1+dp[0]
  for j in range(n-2):
    if dp[j+2]==1:
      dp[j+2]+=(dp[j]+dp[j+1]-1)
  print(dp[-1]%1000000007)