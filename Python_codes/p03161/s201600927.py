def main():
    n, k = map(int, input().split())
    h = [0] + list(map(int, input().split()))

    INF = 10 ** 12
    dp = [INF] * (n + 1)
    dp[1] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i + j <= n:
                dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))

    print(dp[-1])


if __name__ == "__main__":
    main()
