def main():
    s = input()[::-1]
    mod = 13
    p = 10 ** 9 + 7
    dp = [0] * mod
    dp[0] = 1

    for i, ss in enumerate(s):
        tmp = [0] * mod
        if ss == "?":
            for j in range(10):
                d = j * pow(10, i, mod)
                for k in range(mod):
                    tmp[(k + d) % mod] += dp[k]
                    tmp[(k + d) % mod] %= p
        else:
            d = int(ss) * pow(10, i, mod)
            for k in range(mod):
                tmp[(k + d) % mod] += dp[k]
        dp = tmp
    print(dp[5])
if __name__ == '__main__':
    main()
