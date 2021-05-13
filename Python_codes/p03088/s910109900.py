n=int(input())
dp = [[[[0 for i in range(4)]for i in range(4)]for i in range(4)]for i in range(n)]
mod=10**9+7
for i in range(4):
    dp[0][0][0][i]=1

for i in range(n-1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for st in range(4):
                    if i>=1:
                        if k==0 and l==1 and st==2:continue
                        if k==0 and l==2 and st==1:continue
                        if k==1 and l==0 and st==2:continue
                    if i>=2:
                        if j==0 and k==1 and st==2:continue
                        if j==0 and l==1 and st==2:continue
                    dp[i+1][k][l][st] = (dp[i+1][k][l][st]+dp[i][j][k][l])%mod


sum=0
for j in range(4):
    for k in range(4):
        for l in range(4):
            sum = (sum+dp[n-1][j][k][l])%mod

#print(*dp[n-1],sep="\n")
print(sum)
