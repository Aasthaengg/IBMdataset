def main():
    from itertools import product
    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]

    l = [[0, 0], [1, 0], [0, 1], [1, 1]]
    r = range(4)
    ans = - 10 ** 9
    for c in product(r, r, r, r, r):
        v = [l[i] for i in c]
        s = sum(v, [])
        if sum(s) == 0:
            continue
        t = 0
        for x, y in zip(f, p):
            m = sum([i * j for i, j in zip(s, x)])
            t += y[m]

        ans = max(ans, t)

    print(ans)


if __name__ == '__main__':
    main()
