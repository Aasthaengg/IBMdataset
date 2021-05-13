n=int(input())
S=list(input())
dp=[[0]*(n+1) for i in range(n+1)]#i文字目まで、j文字目までの長さ
for i in range(1,n):
  for j in range(i+1,n+1):
    if S[i-1]==S[j-1]:
      if j-i<dp[i-1][j-1]+1:
        dp[i][j]=dp[i-1][j-1]
      else:
        dp[i][j]=dp[i-1][j-1]+1
ans=0
for i in range(n+1):
  for j in range(n+1):
    if dp[i][j]>ans:
      ans=dp[i][j]
print(ans)