def is_ok(arg):
    global K
    return r[arg] >= K
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
N, K = map(int, input().split())
A = [0] * 10**5
for _ in range(N):
    a, b = map(int, input().split())
    A[a-1] += b
r = [A[0]]
for i in range(10**5-1):
    r.append(r[i] + A[i+1])
print(meguru_bisect(-1, 10**5)+1)
