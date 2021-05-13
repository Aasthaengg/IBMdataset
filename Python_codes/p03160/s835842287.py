def main():
    n = int(input())
    hs = list(map(int, input().split()))

    INF = 10 ** 12
    dp = [INF] * n
    dp[0] = 0

    for i in range(0, n):
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(hs[i + 1] - hs[i]))
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(hs[i + 2] - hs[i]))

    print(dp[-1])


if __name__ == "__main__":
    main()
