h,w=map(int,input().split())
wall=[list(input()) for i in range(h)]
dp=[[0 for i in range(w)] for j in range(h)]
dp[0][0]=1
for i in range(h):
  for j in range(w):
    if i==0 and j==0:
      continue
    tmp=0
    if i > 0 and wall[i-1][j]=='.':
      tmp+=dp[i-1][j]
    if j > 0 and wall[i][j-1]=='.':
      tmp+=dp[i][j-1]
    dp[i][j]+=tmp
print(dp[h-1][w-1] % 1000000007)

