import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate
    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    acc = list(accumulate(a))

    ok = n - 1
    ng = -1

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        i = mid
        cur = acc[i]
        while i < n - 1:
            if 2 * cur >= a[i + 1]:
                cur += a[i + 1]
                i += 1
            else:
                break
        if i == n - 1:
            ok = mid
        else:
            ng = mid

    print(n - ok)


if __name__ == '__main__':
    main()
