h,w=map(int,input().split())
l=[]
for i in range(h):
    l.append(list(input()))
dp=[]
for i in range(h):
    dp.append([0]*w)
c=1
for i in range(w):
    if l[0][i]=='#':
        c=0
    dp[0][i]=c
c=1
for i in range(h):
    if l[i][0]=='#':
        c=0
    dp[i][0]=c
for i in range(1,h):
    for j in  range(1,w):
        if l[i][j]=='.':
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
        else:
            dp[i][j]=0
print(dp[h-1][w-1]%1000000007)

        
        
