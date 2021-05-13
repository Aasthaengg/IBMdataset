def solve():
    N = int(input())
    dp = [[0] * 3 for i in range(N + 1)]
    for i in range(N):
        A = list(map(int, input().split()))
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + A[k])
    return max(dp[N])

print(solve())
