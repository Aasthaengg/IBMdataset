NUM=10**9+7
H,W=list(map(int,input().split()))
matrix=[]
for i in range(H):
    matrix.append(list(input()))
dp=[[0]*W for i in range(H)]
dp[0][0]=1
for i in range(1,W):
    if(matrix[0][i]=='#'):
        dp[0][i]=0
    else:
        dp[0][i]=dp[0][i-1]
for j in range(1,H):
    if(matrix[j][0]=='#'):
        dp[j][0]=0
    else:
        dp[j][0]=dp[j-1][0]
for i in range(1,H):
    for j in range(1,W):
        if(matrix[i][j]=='#'):
            dp[i][j]=0
        else:
            dp[i][j]=(dp[i-1][j] + dp[i][j-1])%NUM 
print(dp[H-1][W-1]%NUM)