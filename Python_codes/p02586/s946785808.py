h,w,k = map(int, input().split())
item = [[0 for _ in range(w)] for _ in range(h)]
for i in range(k):
    y,x,v = list(map(int,input().split()))
    item[y-1][x-1]=v

dp = [[[0 for _ in range(w+1)] for _ in range(h+1)] for _ in range(4)]

for y in range(h):
    for x in range(w):
        for i in range(4):
            dp[0][y+1][x]=max(dp[0][y+1][x],dp[i][y][x])
            dp[i][y][x+1]=max(dp[i][y][x+1],dp[i][y][x])
        if item[y][x]>0:
            for i in range(3):
                dp[0][y+1][x]  =max(dp[0][y+1][x],  dp[i][y][x]+item[y][x])
                dp[i+1][y][x+1]=max(dp[i+1][y][x+1],dp[i][y][x]+item[y][x])
ans=dp[0][-1][-2]
print(ans)