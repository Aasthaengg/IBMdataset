def p_d():
    H, W, K = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [0] * W
    dp[0] = 1
    fib = [1, 1]
    for i in range(2, W):
        fib.append(fib[i - 2] + fib[i - 1])
    some = [0] * W
    for i in range(W):
        some[i] = fib[i] * fib[W - i - 1]
    some_2 = [0] * (W - 1)
    for i in range(W - 1):
        some_2[i] = fib[i] * fib[W - i - 2]
    for i in range(1, H + 1):
        w = 0
        NEXT = [0] * W
        for j in range(W):
            if j > 0:
                NEXT[j - 1] += dp[j] * some_2[j - 1]
                NEXT[j - 1] %= mod
            if j < W - 1:
                NEXT[j + 1] += dp[j] * some_2[j]
                NEXT[j + 1] %= mod
            if dp[j] > 0:
                NEXT[j] += dp[j] * some[j]
                NEXT[j] %= mod
            w += 1
        dp = NEXT
    print(dp[K - 1] % mod)


if __name__ == '__main__':
    p_d()
