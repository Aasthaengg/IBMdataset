def totalcost_recur(i,cost,N,lookup):
  if i>=N:
    return 0
  if i in lookup:
      return lookup[i]
  option1 = abs(cost[i]-cost[i+1]) + totalcost_recur(i+1,cost,N,lookup)
  ans = option1
  if i+2<=N:
    option2 = abs(cost[i]-cost[i+2]) + totalcost_recur(i+2,cost,N,lookup)
    ans = min(option2,ans)
  lookup[i] = ans
  return ans



def totalcost_dp(cost,N):
    dp = [0]*(N+1)
    dp[1] = 0
    dp[2] = abs(cost[2]-cost[1])
    i = 3
    while i<=N:
        option1 = dp[i-1]+abs(cost[i]-cost[i-1])
        option2 = dp[i-2]+abs(cost[i]-cost[i-2])
        dp[i] = min(option1,option2)
        i+=1

    return dp[N]


n = int(input())
cost = list(map(int,input().split()))
cost = [0]+cost
lookup = {}

print(totalcost_dp(cost,n))