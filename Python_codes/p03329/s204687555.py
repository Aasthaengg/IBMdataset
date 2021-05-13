import sys 
sys.setrecursionlimit(2147483647)

INF = float("inf")

memo = [float("inf")]*100005

def rec(n):
    if n==0:
        return 0
    if memo[n]!=float("inf"):
        return memo[n]
    res = float("inf")
    val = 1
    while val<=n:
        res = min(res,rec(n-val)+1)
        val*=6
    
    val = 1
    while val<=n:
        res = min(res,rec(n-val)+1)
        val*=9
    memo[n]=res
    return memo[n]

dp = [INF]*100005

def morau_dp():
    #min(dp[n-x]+1....)
    N = int(input())
    dp[0]=0
    for i in range(1,N+1):
        val = 1
        while val<=N:
            dp[i]=min(dp[i],dp[i-val]+1)
            val*=6
        
        val = 1
        while val<=N:
            dp[i] = min(dp[i],dp[i-val]+1)
            val*=9

    print(dp[N])


if __name__ == "__main__":
    # N = int(input())
    # print(rec(N))
    morau_dp()