def main():
    from itertools import product
    n, a, b, c, *l = map(int, open(0).read().split())
    k = ['A', 'B', 'C', 'D']
    cost = []
    for abcd in product(k, repeat=n):
        s, t, u = [], [], []
        for p, q in zip(abcd, l):
            if p == 'A':
                s.append(q)
            elif p == 'B':
                t.append(q)
            elif p == 'C':
                u.append(q)
        tmp = 0
        for p, q in zip([a, b, c], [s, t, u]):
            tmp += abs(p - sum(q)) + 10 * (len(q) - 1)

        if len(s) > 0 and len(t) > 0 and len(u) > 0:
            cost.append(tmp)

    ans = min(cost)
    print(ans)


if __name__ == '__main__':
    main()
