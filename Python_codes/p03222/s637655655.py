import sys
H,W,K=map(int,input().split())
if W==1:
    print(1)
    sys.exit()
L=[1,1,2,3,5,8,13,21,34]
mod=10**9+7
dp=[[0]*W for i in range(H+1)]
dp[0][0]=1
for i in range(H):
    for j in range(W):
        if j==0:
            dp[i+1][j]+=dp[i][j]*L[W-1]
            dp[i+1][j]+=dp[i][j+1]*L[W-2]
            dp[i+1][j]%=mod
        elif j==W-1:
            dp[i+1][j]+=dp[i][j]*L[W-1]
            dp[i+1][j]+=dp[i][j-1]*L[W-2]
            dp[i+1][j]%=mod
        else:
            dp[i+1][j]+=dp[i][j-1]*L[j-1]*L[W-j-1]
            dp[i+1][j]+=dp[i][j]*L[j]*L[W-j-1]
            dp[i+1][j]+=dp[i][j+1]*L[j]*L[W-j-2]
            dp[i+1][j]%=mod
print(dp[H][K-1])