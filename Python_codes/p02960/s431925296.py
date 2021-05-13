def main():
    MOD = 10 ** 9 + 7
    S = input()
    N = len(S)
    mod13 = [0] * 13
    mod13[0] = 1
    exponent = 1
    for i in range(1, N + 1):
        mod13_new = [0] * 13
        c = S[-i]
        if c == "?":
            for n in range(10):
                m = n * exponent % 13
                for r in range(13):
                    mod13_new[(r + m) % 13] += mod13[r]
        else:
            for r in range(13):
                mod13_new[(r + int(c) * exponent) % 13] = mod13[r]
        exponent = exponent * 10 % 13
        for r in range(13):
            mod13_new[r] %= MOD
        mod13 = mod13_new
    print(mod13[5])

if __name__ == "__main__":
    main()