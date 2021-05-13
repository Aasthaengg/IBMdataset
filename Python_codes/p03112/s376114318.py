import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, q = list(map(int, readline().split()))
    s = [0] * (a + 2)
    t = [0] * (b + 2)
    d = [0] * (a + b + 2)

    for i in range(1, a + 1):
        dist = int(input())
        s[i] = dist
        d[i] = (dist, 0)

    s[0] = -INF
    s[a + 1] = INF

    for i in range(1, b + 1):
        dist = int(input())
        t[i] = dist
        d[a + i] = (dist, 1)

    t[0] = -INF
    t[b + 1] = INF

    d[0] = (-INF, 0)
    d[-1] = (INF, 0)

    d.sort()
    d2 = [k[0] for k in d]
    import bisect

    for _ in range(q):
        x = int(input())
        d_idx = bisect.bisect_left(d2, x)
        left = d[d_idx - 1]
        right = d[d_idx]
        res_left = x - left[0]
        res_right = right[0] - x

        if left[1] == 0:
            t_idx = bisect.bisect_left(t, left[0])
            tl = t[t_idx - 1]
            tr = t[t_idx]
            res_left += min(abs(left[0] - tl), abs(tr - left[0]))
        else:
            s_idx = bisect.bisect_left(s, left[0])
            sl = s[s_idx - 1]
            sr = s[s_idx]
            res_left += min(abs(left[0] - sl), abs(sr - left[0]))

        if right[1] == 0:
            t_idx = bisect.bisect_left(t, right[0])
            tl = t[t_idx - 1]
            tr = t[t_idx]
            res_right += min(abs(right[0] - tl), abs(tr - right[0]))
        else:
            s_idx = bisect.bisect_left(s, right[0])
            sl = s[s_idx - 1]
            sr = s[s_idx]
            res_right += min(abs(right[0] - sl), abs(sr - right[0]))
        print(min(res_left, res_right))


if __name__ == '__main__':
    main()
