def main():
    from collections import defaultdict
    n, *a = map(int, open(0).read().split())
    d = defaultdict(lambda: [0, 0])

    ans = 0
    for i, x in enumerate(a, 1):
        d[i + x][0] += 1
        d[i - x][1] += 1
        ans += d[i + x][1] + d[i - x][0]

    print(ans)


if __name__ == '__main__':
    main()
