H,W=map(int,input().split())
A=[]
for _ in range(H):
    a=input()
    A.append(a)
mod=10**9+7

dp=[[0 for i in range(0,W)] for j in range(0,H)]

dp[0][0]=1
for i in range(0,H):
    for j in range(0,W):
        if i!=0 or j!=0:
            if A[i][j]==".":
                ans=0
                if i!=0:
                    ans+=dp[i-1][j]
                if j!=0:
                    ans+=dp[i][j-1]

                dp[i][j]=ans%mod


print(dp[H-1][W-1])