n=int(input())
mod=10**9+7

dp=[[[[0]*5 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[0][0][0][0]=1

for x in range(n):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(1,5):
                    
                    if i==1 and j==2 and l==3:
                        continue
                    if i==1 and k==2 and l==3:
                        continue
                    if j==1 and k==2 and l==3:
                        continue
                    if j==2 and k==1 and l==3:
                        continue
                    if j==1 and k==3 and l==2:
                        continue
                    
                    dp[x+1][j][k][l]=(dp[x+1][j][k][l]+dp[x][i][j][k])%mod
ans=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            ans =(ans+dp[n][i][j][k])%mod

print(ans)

