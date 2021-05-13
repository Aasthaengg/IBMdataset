n,K=list(map(int,input().split()))
xy=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])

dp=[[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        for k in range(i,j+1):
            dp[i][j].append(xy[k][1])
        
        dp[i][j].sort()

ans=10**19

for x in range(K,n+1):
    for i in range(n-x+1):
        left=xy[i][0]
        right=xy[i+x-1][0]

        for j in range(len(dp[i][i+x-1])-K+1):
            down=dp[i][i+x-1][j]
            up=dp[i][i+x-1][j+K-1]

            ans=min(ans,(right-left)*(up-down))

print(ans)
