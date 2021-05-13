N,W=map(int,input().split())
dp=[[-1]*301 for i in range(N+1)]
dp[0][0]=0

for i in range(N):
    w,v=map(int,input().split())
    if i==0:
        base=w
    for i in range(N)[::-1]:
        for j in range(301)[::-1]:
            if dp[i][j]!=-1:
                dp[i+1][j+w-base]=max(dp[i][j]+v,dp[i+1][j+w-base])

ans=0
for index,item in enumerate(dp):
    if W-index*base+1<=0:
        break
    ans=max(max(item[:W-index*base+1]),ans)

print(ans)