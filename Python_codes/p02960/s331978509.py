def main():
    s = input()
    mod = 10 ** 9 + 7

    DP = [[0] * 13 for i in range(len(s) + 1)]
    DP[0][0] = 1
    for ci, c in enumerate(s):
        if c == '?':
            for r in range(13):
                for k in range(10):
                    DP[ci + 1][(r * 10 + k) % 13] += DP[ci][r]
                    DP[ci + 1][(r * 10 + k) % 13] %= mod

        else:
            for r in range(13):
                DP[ci + 1][(r * 10 + int(c)) % 13] += DP[ci][r]
                DP[ci + 1][(r * 10 + int(c)) % 13] %= mod

    print(DP[len(s)][5])


if __name__ == '__main__':
    main()
