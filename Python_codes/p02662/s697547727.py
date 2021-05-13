def resolve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * (s + 1)
    dp[0] = 1
    for i in a:
        for j in range(s - i, -1, -1):
            dp[j + i] = dp[j + i] * 2 + dp[j]
            dp[j + i] %= mod
        for j in range(min(i, s + 1)):
            dp[j] *= 2
            dp[j] %= mod
    print(dp[-1])


if __name__ == '__main__':
    resolve()
