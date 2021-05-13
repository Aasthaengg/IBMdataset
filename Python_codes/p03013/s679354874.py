def main():
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    for _ in range(m):
        a = int(input())
        dp[a] = -1
    mod = 10 ** 9 + 7

    for i in range(n + 1):
        if dp[i] == 0:
            if i - 1 >= 0 and dp[i - 1] != -1:
                dp[i] += dp[i - 1]
            if i - 2 >= 0 and dp[i - 2] != -1:
                dp[i] += dp[i - 2]

    print(dp[-1] % mod)


if __name__ == "__main__":
    main()
