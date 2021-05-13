def main():
    from collections import namedtuple

    Dish = namedtuple('Dish', 'idx x v')

    n, c = map(int, input().split())

    ds = []
    for i in range(n):
        x, v = map(int, input().split())
        ds.append(Dish(idx=i, x=x, v=v))

    gol = [0] * n  # 時計回りの最大値
    s = 0
    ma = 0
    for d in ds:
        s += d.v
        ma = max(ma, s - d.x)
        gol[d.idx] = ma

    gor = [0] * n  # 反時計回りの最大値
    s = 0
    ma = 0
    for d in reversed(ds):
        s += d.v
        ma = max(ma, s - (c - d.x))
        gor[d.idx] = ma

    gol0 = [0] * n  # 時計回りから0に戻ったときのカロリー
    for d in reversed(ds):
        gol0[d.idx] = gol[d.idx] - d.x

    gor0 = [0] * n  # 反時計回りから0に戻ったときのカロリー
    for d in reversed(ds):
        gor0[d.idx] = gor[d.idx] - (c - d.x)

    ret = max(max(gol), max(gor))
    for l in range(n - 1):
        t = gol0[l] + gor[l + 1]
        ret = max(ret, t)

    for r in range(n - 1, 0, -1):
        t = gor0[r] + gol[r - 1]
        ret = max(ret, t)

    print(ret)


if __name__ == '__main__':
    main()
