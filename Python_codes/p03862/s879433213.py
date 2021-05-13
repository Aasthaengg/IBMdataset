def main():
    n, x, *a = map(int, open(0).read().split())
    a = [0] + a
    ans = 0
    tmp = 0
    for i, j in zip(a, a[1:]):
        i -= tmp
        if (i + j - x) > 0:
            c = (i + j - x)
            ans += c
            tmp = c
        else:
            tmp = 0

    print(ans)


if __name__ == '__main__':
    main()
