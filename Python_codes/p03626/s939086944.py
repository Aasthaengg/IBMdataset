def main():
    n = int(input())
    s = input()
    t = input()
    mod = 10 ** 9 + 7

    p = {"||": 2, "==": 3, "|=": 2, "=|": 1, "|": 3, "=": 6}
    ans = 1
    bf = ""
    it = iter(range(n))
    for i in it:
        if s[i] == t[i]:
            nw = "|"
        else:
            nw = "="
            it.__next__()

        ans *= p[bf + nw]
        ans %= mod
        bf = nw

    print(ans % mod)


if __name__ == '__main__':
    main()
