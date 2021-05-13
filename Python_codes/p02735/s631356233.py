h,w=map(int,input().split())
s=[]
for index in range(h):
    s.append(list(str(input())))


#def sur(x):
#    res=[]
#    if x+1<=w-1:
#        res.append((x+1,y))
#    if y+1<=h-1:
#        res.append((x,y+1))
#    return res


dp=[[-1]*w for index1 in range(h)]
if s[0][0]=='.':
    dp[0][0]=0
else:
    dp[0][0]=1

temp=s[0][0]
for index2 in range(1,w):
    if temp=='.' and s[0][index2]=='#':
        dp[0][index2]=dp[0][index2-1]+1
    else:
        dp[0][index2]=dp[0][index2-1]
    temp=s[0][index2]

temp=s[0][0]
for index3 in range(1,h):
    if temp=='.' and s[index3][0]=='#':
        dp[index3][0]=dp[index3-1][0]+1
    else:
        dp[index3][0]=dp[index3-1][0]
    temp=s[index3][0]


for i in range(1,h):
    for j in range(1,w):
        if s[i][j]=='#':
            if s[i-1][j]=='.':
                if s[i][j-1]=='.':
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1)
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1])
            else:
                if s[i][j-1]=='.':
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1]+1)
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])


print(dp[h-1][w-1])


