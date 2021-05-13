def solve():
    #start here
    n = int(input())
    dp = [[0 for i in range(3)] for j in range(n)]
    a, b, c = map(int,input().split())
    dp[0][0], dp[0][1], dp[0][2] = a, b, c
    for i in range(1, n):
        a, b, c = map(int,input().split())
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
        dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + c
    print(max(dp[n-1]))
    
solve()