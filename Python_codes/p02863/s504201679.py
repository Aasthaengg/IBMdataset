def resolve():
    N, T = list(map(int, input().split()))
    AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    dp = [[0 for _ in range(T)] for __ in range(N)]
    for i in range(1, N):
        time, value = AB[i-1]
        for j in range(T-1, -1, -1):
            dp[i][j] = dp[i-1][j]
            if j >= time:
                dp[i][j] = max(dp[i][j], dp[i-1][j-time]+value)
    print(max(dp[i][T-1]+AB[i][1] for i in range(N)))
    
if __name__ == "__main__":
    resolve()

