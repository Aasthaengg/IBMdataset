h,w=map(int,input().split())
m=10**9+7
arr=[[1 for j in range(w)]for i in range(h)]
for i in range(h):
  string=input()
  for j in range(w):
    if string[j]=="#":
      arr[i][j]=0

dp=[[0 for j in range(w)]for i in range(h)]
dp[0][0]=1
for i in range(h):
  for j in range(w):
    if i>0 and arr[i-1][j]:
      dp[i][j]=(dp[i][j]+dp[i-1][j])%m
    if j>0 and arr[i][j-1]:
      dp[i][j]=(dp[i][j]+dp[i][j-1])%m
print(dp[h-1][w-1]%m)    
