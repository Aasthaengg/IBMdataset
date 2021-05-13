import sys
from bisect import bisect_right

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C, D, E, F = map(int, readline().split())

    sugar = set()
    for i in range(F // C + 1):
        for j in range(F // D + 1):
            s = C * i + D * j
            if s <= F:
                sugar.add(s)
            else:
                break

    sugar = sorted(sugar)

    water = set()
    for i in range(F // (100 * A) + 1):
        for j in range(F // (100 * B) + 1):
            w = 100 * A * i + 100 * B * j
            if w <= F:
                water.add(w)
            else:
                break

    water = sorted(water)

    concentration = 0
    ans_water = ans_sugar = 0
    for w in water[1:]:
        s_max = min(F - w, w // 100 * E)
        s = sugar[bisect_right(sugar, s_max) - 1]
        if concentration < 100 * s / (w + s):
            concentration = 100 * s / (w + s)
            ans_water = w
            ans_sugar = s

    if ans_water == 0:
        ans_water = 100 * A

    print(ans_water + ans_sugar, ans_sugar)
    return


if __name__ == '__main__':
    main()
