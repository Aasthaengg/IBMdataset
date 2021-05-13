import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import groupby

    s = input()
    k = int(readline())
    l = len(s)

    if len(set(s)) == 1:
        return print(l * k // 2)

    ans = 0
    gr = [list(g) for k, g in groupby(s)]
    for g in gr:
        ans += len(g) // 2 * k

    if gr[0][0] == gr[-1][-1]:
        ans += ((len(gr[0]) + len(gr[-1])) // 2) * (k - 1)
        ans -= (len(gr[0]) // 2 + len(gr[-1]) // 2) * (k - 1)

    print(ans)


if __name__ == '__main__':
    main()
