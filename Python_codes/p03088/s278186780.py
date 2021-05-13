#122_D
n=int(input())
mod=10**9+7

dp=[[[[0 for _ in range(4)]for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
for k in range(4):
    for l in range(4):
        for m in range(4):
            flg=(k==0 and l==1 and m==2) or (k==0 and l==2 and m==1) or (k==2 and l==0 and m==1)
            if not flg:
                dp[3][k][l][m]=1
        

        
for i in range(4,n+1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    flg=(j==0 and (k==2 or l==2) and m==1) or (k==0 and l==1 and m==2) or (k==0 and l==2 and m==1) or (k==2 and l==0 and m==1)
                    if not flg:
                        dp[i][k][l][m]+=dp[i-1][j][k][l]
ans=0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans+=dp[n][i][j][k]
print(ans%mod)