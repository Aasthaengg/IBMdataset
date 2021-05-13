def solve():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    def is_ok(x):
        res = 0
        for ss in s:
            y = ss // x
            if ss % x == 0:
                y -= 1
            res += y
        return res

    ng = 0
    ok = 10 ** 10
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid) <= k:
            ok = mid
        else:
            ng = mid

    print(ok)


solve()
