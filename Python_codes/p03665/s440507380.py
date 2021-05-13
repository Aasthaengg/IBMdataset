N,P = map(int,input().split())
a_ls = list(map(int, input().split()))

# dp[i][j] := i-1番目のbuiscuitsまでみて、食べた枚数のあまりがjであるような方法の数
dp = [[0,0] for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    next = (a_ls[i-1])%2
    if next == 0:
        dp[i][0] += 2 * dp[i-1][0]
        dp[i][1] += 2 * dp[i-1][1]
    else:
        dp[i][0] += dp[i-1][0] + dp[i-1][1]
        dp[i][1] += dp[i-1][0] + dp[i-1][1]
print(dp[-1][P])
        
