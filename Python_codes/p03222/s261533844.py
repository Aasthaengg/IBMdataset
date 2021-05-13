def main():
    h, w, k = map(int, input().split())
    MOD = 10 ** 9 + 7

    patterns = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    x = [0] * (w - 1)
    for i in range(w-1):
        x[i] = patterns[i] * patterns[max(0, w-i-2)]

    y = [0] * w
    for i in range(w):
        y[i] = patterns[i] * patterns[max(0, w-i-1)]

    dp = [[0] * w for _ in range(h+1)]
    dp[0][0] = 1
    for j in range(h):
        for i in range(w):
            d = dp[j][i] * y[i]
            if i - 1 >= 0:
                d += dp[j][i-1] * x[i-1]
            if i + 1 < w:
                d += dp[j][i+1] * x[i]
            dp[j+1][i] = d % MOD
    print(dp[h][k-1])


main()
