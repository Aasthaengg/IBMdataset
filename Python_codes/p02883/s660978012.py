n,k=map(int,input().split())
*a,= map(int,input().split())
*f,= map(int,input().split())
a=sorted(a)
f=sorted(f, reverse=True)

def is_ok(arg):
    cnt=0
    for i in range(n):
        cnt+=max(a[i]-arg//f[i], 0)
    return cnt<=k

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(-1, 10**12))