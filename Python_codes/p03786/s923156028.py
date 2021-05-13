n = int(input())
a = list(map(int, input().split()))
a.sort()
def solve(i):
    size = sum(a[:i+1])
    for j in range(i+1, n):
        if a[j]>2*size:
            return False
        size += a[j]
    return True

ok = n-1
ng = -1
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(n-ok)