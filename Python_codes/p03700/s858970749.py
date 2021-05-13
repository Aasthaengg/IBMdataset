N, A, B, *X = map(int, open(0).read().split())

ub = 10 ** 15
lb = 0
while ub - lb > 1:
    mid = (ub + lb) // 2
    cnt = 0
    for i in range(N):
        if X[i] - B * mid > 0:
            cnt += -(-(X[i] - B * mid) // (A - B))

    if cnt > mid:
        lb = mid
    else:
        ub = mid

print(ub)
