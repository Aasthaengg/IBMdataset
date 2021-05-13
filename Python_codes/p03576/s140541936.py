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
            if xarr[xi] <= x and x <= xarr[xj] and yarr[yi] <= y and y <= yarr[yj]:
                res += 1
        return res

    ans = 5*10**18
    for xi in range(n-1):
        for xj in range(xi+1, n):
            for yi in range(n-1):
                for yj in range(yi+1, n):
                    if count_inside(xi, xj, yi, yj) >= k:
                        area = (xarr[xj] - xarr[xi]) * (yarr[yj] - yarr[yi])
                        ans = min(ans, area)
    print(ans)

if __name__ == '__main__':
    abc075_d()