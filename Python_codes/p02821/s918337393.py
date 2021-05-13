import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    a.sort()

    import bisect

    ok = 0
    ng = 2 * max(a) + 1

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        count = 0
        i = 0
        for elem in a:
            minlim = mid - elem
            count += (n - bisect.bisect_left(a, minlim))

        if count >= m:
            ok = mid
        else:
            ng = mid

    from itertools import accumulate

    a_cum = list(accumulate(a[::-1]))
    a_cum = a_cum[::-1] + [0]
    ans = 0
    j = n
    cnt_over = 0

    for elem in a:
        minlim = ok - elem + 1
        idx = bisect.bisect_left(a, minlim)
        ans += a_cum[idx]
        ans += elem * (n - idx)
        cnt_over += (n - idx)

    ans += ok * (m - cnt_over)

    print(ans)


if __name__ == '__main__':
    main()
