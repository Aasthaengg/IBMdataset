def coins(n,prob):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(i+1):

            if j == 0:
                dp[i][j] = dp[i-1][j]*(1-prob[i-1])
            else:
                dp[i][j] = dp[i-1][j]*(1-prob[i-1])+dp[i-1][j-1]*prob[i-1]
    total = 0
    for i in range(n,n//2,-1):
        total+= dp[n][i]
    return total

n = int(input())
prob = list(map(float,input().split()))
print(coins(n,prob))