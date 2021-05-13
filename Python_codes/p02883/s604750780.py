import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

a = sorted(a)
f = sorted(f,reverse = True)

hq = []

def is_ok(checking):
    cost = 0
    for i in range(n):
        cost += max(0,math.ceil((a[i]*f[i]-checking)/f[i]))
    if cost <= k:
        return True
    else:
        return False

def meguru_bisect(ng, ok):
    while (abs(ok-ng)>1):
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ok = meguru_bisect(-1, 1e+12+1) 
print(int(ok))
# 初期値の範囲は取りえる値-1～+1とする←範囲内はok,ngどちらもあり得るため