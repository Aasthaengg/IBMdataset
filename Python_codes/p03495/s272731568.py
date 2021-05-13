def main():
    from collections import Counter

    n, k, *a = map(int, open(0).read().split())
    c = Counter(a).values()
    v = len(c) - k
    l = list(c)
    l.sort()
    ans = sum(l[:v])
    print(ans)


if __name__ == '__main__':
    main()
