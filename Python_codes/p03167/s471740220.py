H,W=map(int,input().split())
L=[]
for i in range(H):
    l=input()
    L.append(l)
dp=[[0]*(W+1) for i in range(H+1)]
dp[1][1]=1
for i in range(1,H+1):
    for j in range(1,W+1):
        if L[i-1][j-1]==".":
            dp[i][j]=dp[i][j]+dp[i][j-1]+dp[i-1][j]
print(dp[-1][-1]%(10**9+7))

