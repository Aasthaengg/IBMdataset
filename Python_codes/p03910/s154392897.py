import sys
sys.setrecursionlimit(10**7)
def is_ok(m, n):
    return m*(m+1)//2>=n
def meguru_bisect(ng, ok, n):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, n):
            ok = mid
        else:
            ng = mid
    return ok
def f(n):
    if n>0:
        m = meguru_bisect(0,10**7, n)
        print(m)
        f(n-m)
N = int(input())
f(N)
