def main():
    n, *a = map(int, open(0).read().split())
    p, q = min(a), max(a)

    if p == q:
        print(0)
        exit()

    x = []
    f, g = a.index(p) + 1, a.index(q) + 1
    if abs(p) > abs(q):
        for i in range(n):
            if a[i] > 0:
                x.append((f, i + 1))
        for i in range(n - 1):
            x.append((n - i, n - i - 1))

    else:
        for i in range(n):
            if a[i] < 0:
                x.append((g, i + 1))
        for i in range(n - 1):
            x.append((i + 1, i + 2))

    print(len(x))
    print('\n'.join(['{} {}'.format(i[0], i[1]) for i in x]))


if __name__ == '__main__':
    main()
