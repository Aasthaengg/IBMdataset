mod=round(1e9+7)

r,c = list(map(int, input().split()))
mat = []
for i in range(r):
    mat.append(list(input()))
dp=[]
for i in range(r):
    dp.append([0]*(c))
for i in range(r):
    if mat[i][0]=='#':
        break
    else:
        dp[i][0]=1
for i in range(c):
    if mat[0][i]=='#':
        break
    else:
        dp[0][i]=1
for i in range(1,r):
    for j in range(1,c):
        if mat[i][j]=='#':
            dp[i][j]=0
        else:
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
print(dp[r-1][c-1])
    
