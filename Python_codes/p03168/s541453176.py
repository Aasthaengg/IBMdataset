def solve():
    N = int(input())
    p = list(map(float,input().split()))

    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1.0

    for i in range(N):
        for j in range(0,i+1):
            dp[i+1][j+1] += dp[i][j] * p[i]
            dp[i+1][j] += dp[i][j] * (1.0 -p[i])
    

    ans = 0
    for i in range(N+1):
        if i > (N-i):
            ans += dp[-1][i]
    
    print(ans)
            
if __name__ == '__main__':
    solve()