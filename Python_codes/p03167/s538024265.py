#F
H,W=map(int,input().split())
A=[[x for x in input()] for i in range(H)]
mod=10**9+7

dp=[[0 for i in range(W+1)] for j in range(H+1)]
dp[H-1][W-1]=1

for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if i==H-1 and j==W-1:
            continue
        
        if A[i][j]=="#":
            continue
        elif A[i][j]==".":
            dp[i][j]=(dp[i+1][j]+dp[i][j+1])%mod

print(dp[0][0])