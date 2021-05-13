def main():
    n, k, *v = map(int, open(0).read().split())
    w = v[::-1]

    ans = 0
    m = min(n, k)
    for i in range(m + 1):
        for j in range(m + 1 - i):
            d = k - (i + j)
            g = v[:i] + w[:j]
            ps = sum(x for x in g if x > 0)
            ng = [x for x in g if x < 0]
            ng.sort()
            val = ps + sum(ng[d:])
            ans = max(ans, val)

    print(ans)


if __name__ == '__main__':
    main()
