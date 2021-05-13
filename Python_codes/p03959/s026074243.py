def main():
    mod = 10 ** 9 + 7

    n = int(input())
    *t, = map(int, input().split())
    *a, = map(int, input().split())

    if t[-1] != a[0]:
        # 高橋と青木の見た山の高さの最大値が一致しない
        print(0)
        return

    ret = 1

    # [lo,hi]
    for i in range(n):
        if i == 0:
            lo = hi = t[i]
        else:
            if t[i - 1] < t[i]:
                # 山iの高さは一意に定まる
                lo = hi = t[i]
            elif t[i - 1] == t[i]:
                # [1,t[i]]の範囲で自由に選べる
                lo = 1
                hi = t[i]
            else:
                # t[i - 1] > t[i]:
                print(0)
                return

        if i == n - 1:
            lo = max(lo, a[i])
            hi = min(hi, a[i])
        else:
            if a[i] > a[i + 1]:
                # 山iの高さは一意に定まる
                lo = max(lo, a[i])
                hi = min(hi, a[i])
            elif a[i] == a[i + 1]:
                # [1,a[i]]の範囲で自由に選べる
                lo = max(lo, 1)
                hi = min(hi, a[i])
            else:
                # a[i] < a[i + 1]:
                print(0)
                return

        if lo > hi:
            print(0)
            return

        ret = ret * (hi - lo + 1) % mod

    print(ret)


if __name__ == '__main__':
    main()
