def main():
    from math import ceil
    n, h, *ab = map(int, open(0).read().split())

    *c, = map(lambda x: -x, ab[::2])
    d = sorted(c + ab[1::2], key=abs, reverse=True)
    ans = 0
    for x in d:
        if x < 0:
            ans += ceil(h / abs(x))
            break

        h -= x
        ans += 1
        if h <= 0:
            break

    print(ans)


if __name__ == '__main__':
    main()
