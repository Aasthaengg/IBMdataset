n,m=map(int,input().split())
a=[int(i) for i in input().split()]
cost=[2,2,5,5,4,5,6,3,7,6]

dp=[0 for i in range(n+1)]

for i in range(1,n+1):
    p=0
    for j in a:
        if i-cost[j]>=0 and (dp[i-cost[j]]!=0 or i-cost[j]==0):
            p=max(p,int(dp[i-cost[j]]*10+j))
    dp[i]=p

print(dp[n])