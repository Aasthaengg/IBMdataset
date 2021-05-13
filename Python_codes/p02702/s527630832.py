def main():
    s = input()
    mod = 2019

    n = 0
    R = [0] * mod
    R[0] += 1
    for i in range(len(s)):
        n += int(s[-i - 1]) * pow(10, i, mod)
        R[n % mod] += 1

    print(sum([r * (r - 1) // 2 for r in R]))


if __name__ == '__main__':
    main()
