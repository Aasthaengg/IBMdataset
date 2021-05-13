def main():
    n = int(input())
    INF = 10 ** 12
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        j = 6
        while True:
            if i - j < 0:
                break
            dp[i] = min(dp[i], dp[i - j] + 1)
            j *= 6
        k = 9
        while True:
            if i - k < 0:
                break
            dp[i] = min(dp[i], dp[i - k] + 1)
            k *= 9

    print(dp[-1])


if __name__ == "__main__":
    main()
