n=int(input())
dp=[[0 for _ in range(3)] for _ in range(n)]
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
dp[0]=a[0]
for i in range(1,n):
  for j in range(3):
    dp[i][j]=a[i][j]+max(dp[i-1][j-1],dp[i-1][j-2])
print(max(dp[-1]))