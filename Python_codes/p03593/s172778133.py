import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    h, w = map(int, readline().split())
    c = Counter()
    res = [[""] * w for _ in range(h)]

    for _ in range(h):
        s = list(input())
        c.update(s)

    d = Counter()

    if h % 2 == 1 and w % 2 == 1:
        d[1] = 1
        d[2] = (h - 1) // 2 + (w - 1) // 2
    elif h % 2 == 1 and w % 2 == 0:
        d[1] = 0
        d[2] = w // 2
    elif h % 2 == 0 and w % 2 == 1:
        d[1] = 0
        d[2] = h // 2
    d[4] = (h * w - d[1] - 2 * d[2]) // 4

    keys = c.keys()

    for key in keys:
        if c[key] % 2 == 1:
            c[key] -= 1
            d[1] -= 1

    for key in keys:
        if c[key] % 4 == 2:
            c[key] -= 2
            d[2] -= 1

    for key in keys:
        if c[key] % 4 == 0:
            d[4] -= c[key] // 4
            c[key] = 0

    while d[2] > 0:
        d[2] -= 2
        d[4] += 1

    if d[1] == d[2] == d[4] == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
