N, A, B, *H = map(int, open(0).read().split())

def is_ok(K):
    return sum(max(0, -(-(h - B * K) // (A - B))) for h in H) <= K

ng, ok = 0, 10 ** 9
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)