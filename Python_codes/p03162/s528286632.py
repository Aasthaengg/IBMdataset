def main():
    N = int(input())
    ABC = [[int(i) for i in input().split()] for j in range(N)]
    dp = [[0]*3 for _ in range(N+1)]

    for i in range(N):
        for j in range(3):
            dp[i+1][j] = max(dp[i][(j+1) % 3], dp[i][(j+2) % 3]) + ABC[i][j]

    print(max(dp[N]))


if __name__ == '__main__':
    main()
