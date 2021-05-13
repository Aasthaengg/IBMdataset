def abc075_d():
    n, k = map(int, input().split())
    P = []
    xarr = []
    yarr = []
    for _ in range(n):
        x, y = (int(x) for x in input().split())
        P.append((x, y))
        xarr.append(x)
        yarr.append(y)
    xarr.sort()
    yarr.sort()

    def count_inside(xi, xj, yi, yj)->int:
        res = 0
        for x, y in P:
            if xi <= x and x <= xj and yi <= y and y <= yj:
                res += 1
        return res

    ans = 5*10**18
    for s, xi in enumerate(xarr):
        for xj in xarr[s+1:]:
            for t, yi in enumerate(yarr):
                for yj in yarr[t+1:]:
                    if count_inside(xi, xj, yi, yj) >= k:
                        area = (xj - xi) * (yj - yi)
                        ans = min(ans, area)
    print(ans)

if __name__ == '__main__':
    abc075_d()