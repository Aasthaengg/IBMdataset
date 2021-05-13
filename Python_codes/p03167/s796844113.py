h,w=map(int,input().split())
li=[]
for i in range(h):
    li.append(input())
#print(li)
dp=[[0 for i in range(w+1)] for i in range(h+1)]
dp[h-1][w-1]=1
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if li[i][j]=='#':
            dp[i][j]=0
        else:
            if i==(h-1) and j==(w-1):
                dp[i][j]=1
            else:
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
print(dp[0][0]%(10**9+7))