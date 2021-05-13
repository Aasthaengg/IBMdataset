n,C=map(int,input().split())
dp=[[0 for i in range(100002)] for j in range(31)]
for i in range(n):
  s,t,c=map(int,input().split())
  t+=1
  dp[c][s]+=1
  dp[c][t]-=1
nm=[0 for i in range(100002)]
for i in range(31):
  s=1
  for j in range(1,100002):
    dp[i][j]+=dp[i][j-1]
    if dp[i][j]==0 and dp[i][j-1]==1:
      nm[s]+=1
      nm[j]-=1
    elif dp[i][j]==1 and dp[i][j-1]==0:
      s=j
for i in range(1,100002):
  nm[i]+=nm[i-1]
print(max(nm))