import math
n, k = map(int, input().split())
a = [int(input()) for _ in [None]*n]

lb = max(a)
ub = lb * n

while True:
    mid = (ub+lb) // 2
    remain = k - 1
    cw = 0
    for w in a:
        cw += w
        if cw > mid:
            remain -= 1
            cw = w
        if remain < 0:
            break
    if remain < 0:
        if lb == mid:
            print(lb+1)
            break
        lb = mid
    else:
        if lb == mid:
            print(lb)
            break
        ub = mid