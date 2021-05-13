import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    f = list(map(int, readline().split()))

    a.sort()
    f.sort(reverse=True)

    x = [p * q for p, q in zip(a, f)]
    mx = max(x)
    ng = -1
    ok = mx
    import math

    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        rem = k
        for p, q in zip(a, f):
            r = math.floor(mid / q)
            h = max(0, p - r)
            rem -= h
        if rem >= 0:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == '__main__':
    main()
