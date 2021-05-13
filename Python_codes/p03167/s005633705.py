r,c=map(int,input().split())
m=[]
for i in range(r):
    m.append(list(input()))
dp=[[0 for j in range(c)] for i in range(r)]

dp[0][0]=1
for i in range(0,r):
    for j in range(0,c):
        if m[i][j]=='.':
            dp[i][j]+=(dp[i-1][j]+dp[i][j-1])
        

print((dp[r-1][c-1])%(1000000007))