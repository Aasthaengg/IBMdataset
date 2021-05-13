def main():
    N = int(input())
    v = [list(map(int,input().split())) for _ in range(N)]
    dp = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = max(dp[i][1],dp[i][2]) + v[i][0]
        dp[i+1][1] = max(dp[i][0],dp[i][2]) + v[i][1]
        dp[i+1][2] = max(dp[i][0],dp[i][1]) + v[i][2]
    print(max(dp[N][i] for i in range(3)))
    
main()