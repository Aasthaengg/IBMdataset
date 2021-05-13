h,w=map(int,input().split())
mat=[]
dp=[]
dp.append([0]*(w+1))

for i in range(h):
    l=input()
    mat.append(l)
    dp.append([0]*(w+1))

dp[0][1]=1
for i in range(h):
    for j in range(w):
        if mat[i][j]=='.':
            dp[i+1][j+1]=(dp[i][j+1]+dp[i+1][j])%1000000007
            

print(dp[h][w])