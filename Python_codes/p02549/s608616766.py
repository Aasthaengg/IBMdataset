def main():
    n, k = map(int, input().split())
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = -1
    left = [0] * k
    right = [0] * k
    for i in range(k):
        left[i], right[i] = map(int, input().split())
        right[i] += 1
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        for j in range(k):
            if i + left[j] <= n:
                dp[i + left[j]] += dp[i]
            if i + right[j] <= n:
                dp[i + right[j]] -= dp[i]
        dp[i] %= mod
    print(dp[n])


if __name__ == '__main__':
    main()
