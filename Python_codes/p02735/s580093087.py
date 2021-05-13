h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

#solution:dp

dp=[[float('inf') for _ in range(w)] for _ in range(h)]
dp[0][0] = 0 if s[0][0] == '.' else 1

def update(dp, i, j, ni, nj):
    if s[ni][nj]=='.':
        dp[ni][nj]=min(dp[i][j],dp[ni][nj])
    elif s[i][j]=='#':
        dp[ni][nj]=min(dp[i][j],dp[ni][nj])
    else:
        dp[ni][nj]=min(dp[i][j]+1,dp[ni][nj])
    
for i in range(h):
    for j in range(w):
        if i+1<h:
            update(dp,i,j,i+1,j)
        if j+1<w:
            update(dp,i,j,i,j+1)
print(dp[h-1][w-1])