import sys,bisect
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

b = [0]*(n+1)
for i in range(n-1,-1,-1):
    b[i] = a[i]+b[i+1]

ok = 0
ng = 200001

while ng-ok > 1:
    mid = (ok+ng)//2
    cnt = 0
    for e in a:
        k = bisect.bisect_left(a,mid-e)
        cnt += n-k
    if cnt >= m:
        ok = mid
    else:
        ng = mid

c = 0
res = 0

for e in a:
    k = bisect.bisect_left(a,ok+1-e)
    res += b[k] + e*(n-k)
    c += n-k

res += ok*(m-c)
print(res)

