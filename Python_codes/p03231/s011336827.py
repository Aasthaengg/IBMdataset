def main():
    from fractions import gcd

    n, m = map(int, input().split())
    s, t = input(), input()
    l = n * m // gcd(n, m)
    a = [l // n * i + 1 for i in range(n)]
    b = [l // m * i + 1 for i in range(m)]
    c = set(a) & set(b)
    for x in list(c):
        i = a.index(x)
        j = b.index(x)

        if s[i] != t[j]:
            print(-1)
            exit()
    else:
        print(l)


if __name__ == '__main__':
    main()
