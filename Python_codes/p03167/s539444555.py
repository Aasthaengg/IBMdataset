n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
dp=[[0 for i in range(m)]for i in range(n)]
for i in range(n):
    if l[i][0]=="#":
        break
    else:
        dp[i][0]=1
for j in range(m):
    if l[0][j]=="#":
        break
    else:
        dp[0][j]=1
        
for i in range(1,n):
    for j in range(1,m):
        if l[i][j]!="#":
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1]%(10**9+7))