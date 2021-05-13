def main():
    from collections import deque
    from itertools import product

    a, b, c, d, e, f = map(int, input().split())

    water_a = []

    i = 0
    while i * a * 100 <= f:
        water_a.append(i * a * 100)
        i += 1

    water = []
    for w in water_a:
        i = 0
        while i * b * 100 + w <= f:
            water.append(i * b * 100 + w)
            i += 1

    sugar_c = []
    i = 0
    while i * c <= f:
        sugar_c.append(i * c)
        i += 1

    sugar = []
    for s in sugar_c:
        i = 0
        while i * d + s <= f:
            sugar.append(i * d + s)
            i += 1

    conc = -1
    ans = None
    for w, s in product(water, sugar):
        if w + s == 0: continue
        if w + s > f: continue
        if s > w // 100 * e: continue
        t_conc = 100 * s / (w + s)
        if t_conc > conc:
            conc = t_conc
            ans = w + s, s
    print(*ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
#
# sys.setrecursionlimit(10 ** 7)
#
# (int(x)-1 for x in input().split())
# rstrip()
