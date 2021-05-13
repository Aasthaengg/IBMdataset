def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = A[0][0]

    for r in range(2):
        for c in range(N):
            if r != 0:
                dp[r][c] = max(dp[r - 1][c] + A[r][c], dp[r][c])
            if c != 0:
                dp[r][c] = max(dp[r][c - 1] + A[r][c], dp[r][c])
    print(dp[1][N - 1])


if __name__ == '__main__':
    main()
