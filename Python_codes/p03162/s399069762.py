d = int(input())
m=[]
for _ in range(d):
    x=list(map(int,input().split()))
    m.append(x)

dp=[[-1]*3 for i in range(d)]
dp[0][0]=0
dp[0][1]=0
dp[0][2]=0
n=d
for i in range(1,n):
    for j in range(3):
        dp[i][j] = max(dp[i-1][j-1]+m[i-1][j-1],dp[i-1][j-2]+m[i-1][j-2])

ans = max(dp[n-1][0]+m[n-1][0],dp[n-1][1]+m[n-1][1],dp[n-1][2]+m[n-1][2])

# print(md)
print(ans)