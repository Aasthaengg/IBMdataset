def main():
    N = int(input())
    P = [float(i) for i in input().split()]
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[1][1] = P[0]
    dp[1][0] = 1 - P[0]
    for i in range(2, N+1):
        p = P[i-1]
        for j in range(i+1):
            p1 = dp[i-1][j-1] * p if j != 0 else 0
            p2 = dp[i-1][j] * (1 - p)
            dp[i][j] = p1 + p2
    ans = 0
    for j in range(0--N//2, N+1):
        ans += dp[N][j]
    print(ans)


if __name__ == '__main__':
    main()
