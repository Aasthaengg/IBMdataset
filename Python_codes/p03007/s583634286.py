def main():
    from bisect import bisect_left

    n = int(input())
    *a, = map(int, input().split())

    a.sort()

    i0 = bisect_left(a, 0)
    # 0以上の値を指す最小のindex
    # [0,i0) : 負
    # [i0,n) : 正

    sum_ = 0
    if i0 == 0:
        # 0以上のみ
        # [-++...+]
        # [S...E]
        # E-(S-1-2-...)
        ret = []
        s = a[0]
        e = a[-1]
        for x in a[1:-1]:
            ret.append((s, x))
            s -= x
        ret.append((e, s))
        e -= s
        sum_ = e

    elif i0 == n:
        # 負のみ
        # [--...-+]
        # [...S]
        # S-1-2-...
        ret = []
        s = a[-1]
        for x in a[:-1]:
            ret.append((s, x))
            s -= x
        sum_ = s

    else:
        # 正負混在
        # [--...-++...+]
        # [Mm...mp...pP]
        # (P-m-m...)-(M-p-p...)
        ret = []
        m = a[0]
        for x in a[i0:-1]:
            ret.append((m, x))
            m -= x

        p = a[-1]
        for x in a[1:i0]:
            ret.append((p, x))
            p -= x

        ret.append((p, m))
        sum_ = p - m

    print(sum_)
    for row in ret:
        print(*row)


if __name__ == '__main__':
    main()
