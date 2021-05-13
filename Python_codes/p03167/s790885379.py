h,w=map(int,input().split())
a=[input() for _ in range(h)]
dp=[[0]*w for _ in range(h)]
dp[0][0]=1
mod=10**9+7
for i in range(h):
    for j in range(w):
        if i<h-1:
            if a[i+1][j]==".":
                dp[i+1][j]+=dp[i][j]
                dp[i+1][j]%=mod
        if j<w-1:
            if a[i][j+1]==".":
                dp[i][j+1]+=dp[i][j]
                dp[i][j+1]%=mod
print(dp[h-1][w-1])