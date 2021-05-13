import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import groupby
    s = input()
    ans = 0
    prev = 0

    for k, g in groupby(s):
        l = len(list(g))
        if k == "<":
            ans += l * (l + 1) // 2
            prev = l
        else:
            ans += l * (l + 1) // 2
            ans -= min(l, prev)

    print(ans)


if __name__ == '__main__':
    main()
