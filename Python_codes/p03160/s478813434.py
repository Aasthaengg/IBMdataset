def main():
    n = int(input())
    hs = list(map(int, input().split()))

    INF = 10 ** 12
    dp = [INF] * n
    dp[0] = 0
    dp[1] = abs(hs[1] - hs[0])

    for i in range(2, n):
        dp[i] = min(dp[i], dp[i - 1] + abs(hs[i] - hs[i - 1]))
        dp[i] = min(dp[i], dp[i - 2] + abs(hs[i] - hs[i - 2]))

    print(dp[-1])


if __name__ == "__main__":
    main()
