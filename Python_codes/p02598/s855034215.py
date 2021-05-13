def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    c = 0
    for x in a:
        c += -(-x//arg) - 1
    return c <= k

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(meguru_bisect(0,10**9+1))