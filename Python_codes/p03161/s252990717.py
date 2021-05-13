
def totalcost_dp(cost,N,k):
    dp = [float('inf')]*(N+1)
    dp[1] = 0
    
    
    for i in range(1,N+1):
        
        for j in range(i+1,k+i+1):
            if j < N+1:
                dp[j] = min(dp[j],dp[i]+abs(cost[i]-cost[j]))
                
    return dp[N]


n ,k= map(int,input().split())
cost = list(map(int,input().split()))
cost = [0]+cost
print(totalcost_dp(cost,n,k))