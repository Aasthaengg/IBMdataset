def meg_bisect(ng, ok, func):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

n, k, *a = map(int, open(0).read().split())
print(meg_bisect(0, max(a), lambda x: sum(0--b // x - 1 for b in a) <= k))