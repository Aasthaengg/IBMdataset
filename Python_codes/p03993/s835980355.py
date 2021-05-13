import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict
    N = int(readline())
    a = list(map(int, readline().split()))

    d = dict()

    for i, x in enumerate(a, 1):
        d[i] = x

    ans = 0
    for i, x in enumerate(a, 1):
        if d[x] == i:
            ans += 1

    ans //= 2

    print(ans)


if __name__ == '__main__':
    main()
