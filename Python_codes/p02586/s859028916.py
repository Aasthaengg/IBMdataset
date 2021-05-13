def pri(x):
    for item in x:
        print(item)

r,c,k=map(int,input().split())

fuck=[list(map(int,input().split())) for _ in range(k)]

rck=[[0]*(c+1) for _ in range(r+1)]

for [rr,cc,kk] in fuck:
    rck[rr][cc]=kk
#pri(rck)
#dp[y][x][cnt]

dp=[[0]*4 for _ in range(c+1)]
#print(dp)
for y in range(1,r+1):
    for x in range(1,c+1):
        
        dp[x][0]=max(dp[x-1][0],dp[x][0],dp[x][1],dp[x][2],dp[x][3])
        dp[x][1]=max(dp[x][0]+rck[y][x],dp[x][1],dp[x-1][1])
        dp[x][2]=max(dp[x-1][1]+rck[y][x],dp[x][2],dp[x-1][2],dp[x][1])
        dp[x][3]=max(dp[x-1][2]+rck[y][x],dp[x][3],dp[x-1][3],dp[x][2])
        #print(y,x,dp)

print(max(dp[-1]))
             
             
