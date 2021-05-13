n=int(input())
a=list(map(int,input().split()))
cost=[]
for i,g in enumerate(a):
    cost.append([g,i])
cost.sort(reverse=True)

dp=[[0] *(n+1) for _ in range(n+1) ]

for i in range(n):
    for j in range(i+1):
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+cost[i][0]*abs(cost[i][1]-j))
        dp[i+1][j]=max(dp[i+1][j],dp[i][j]+cost[i][0]*abs((n-1-(i-j))-cost[i][1]))

print(max(dp[n]))