def main():
    h, w, *ca = map(int, open(0).read().split())
    it = zip(*[iter(ca[:100])] * 10)
    *c, = map(lambda i: list(i), it)
    a = ca[100:]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    ans = 0
    cost = {i: c[i][1] for i in [0, 2, 3, 4, 5, 6, 7, 8, 9]}
    cost.update({-1: 0, 1: 0})

    for i in a:
        ans += cost[i]

    print(ans)


if __name__ == '__main__':
    main()
