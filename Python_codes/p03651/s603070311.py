import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from math import gcd
    from functools import reduce

    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    a.sort()

    if a[-1] < k:
        return print("IMPOSSIBLE")

    if n == 1:
        if a[0] == k:
            return print("POSSIBLE")
        else:
            return print("IMPOSSIBLE")
    else:
        g = reduce(gcd, a)
        if k % g == 0:
            return print("POSSIBLE")
        else:
            return print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
