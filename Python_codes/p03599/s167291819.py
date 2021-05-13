import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    wa, wb, sa, sb, sol, lim = list(map(int, readline().split()))
    wa *= 100
    wb *= 100

    water = []
    sugar = []

    for wac in range(lim // wa + 1):
        cw = wa * wac
        for wbc in range(30):
            wadd = cw + wb * wbc
            if wadd <= lim:
                water.append(wadd)
            else:
                break

    for sac in range(3001):
        cs = sa * sac
        if cs > lim:
            break
        for sbc in range(3001):
            sadd = cs + sb * sbc
            if sadd <= lim:
                sugar.append(sadd)
            else:
                break

    water = list(set(water))
    sugar = list(set(sugar))
    water.sort()
    sugar.sort()

    import bisect

    maxconc = 0
    ans = [0] * 2

    for ww in water[1:]:
        res = min(sol * ww // 100, lim - ww)
        if res < 0:
            continue

        idx = bisect.bisect_right(sugar, res) - 1

        if idx >= 0:
            sw = sugar[idx]

        conc = (100 * sw) / ww

        if conc >= maxconc:
            maxconc = conc
            ans[0] = (ww + sw)
            ans[1] = sw

    print(*ans)


if __name__ == '__main__':
    main()
