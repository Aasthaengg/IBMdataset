def solve():
    n = int(input())
    X, Y, H = [], [], []
    for i in range(n):
        x, y, h = map(int, input().split())
        X.append(x), Y.append(y), H.append(h)

    for cx in range(101):
        for cy in range(101):
            res = []
            for x, y, h in zip(X, Y, H):
                if h == 0:
                    continue
                hh = h + abs(x - cx) + abs(y - cy)
                res.append(hh)
            if len(set(res)) == 1:
                flg = True
                for x, y, h in zip(X, Y, H):
                    if h != max(res[0] - abs(x - cx) - abs(y - cy), 0):
                        flg = False
                if flg:
                    print(cx, cy, res[0])

solve()