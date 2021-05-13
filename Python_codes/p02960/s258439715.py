def main():
    MOD = 10 ** 9 + 7
    S = input()
    N = len(S)
    mod13 = [[0] * 13 for _ in range(N + 1)]
    mod13[0][0] = 1
    exponent = 1
    for i in range(1, N + 1):
        c = S[-i]
        if c == "?":
            for n in range(10):
                m = n * exponent % 13
                for r in range(13):
                    mod13[i][(r + m) % 13] += mod13[i - 1][r]
        else:
            m = int(c) * exponent % 13
            for r in range(13):
                mod13[i][(r + m) % 13] = mod13[i - 1][r]
        exponent = exponent * 10 % 13
        for r in range(13):
            mod13[i][r] %= MOD
    print(mod13[N][5])

if __name__ == "__main__":
    main()