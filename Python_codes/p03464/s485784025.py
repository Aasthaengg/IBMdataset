k = int(input())
a = list(map(int,input().split()))
def g(x):
    for i in range(k):
        x = (x//a[i])*a[i]
    return x
#最小値を求める
l,r = 0,2+k*max(a)
while abs(r-l) > 1:
    mid = (l+r)//2
    if g(mid) >=2:
        r = mid
    else:
        l = mid
m = r
#最大値を求める
l,r = 0,2+k*max(a)
while abs(r-l) > 1:
    mid = (l+r)//2
    if g(mid) <= 2:
        l = mid
    else:
        r = mid
M = l
if m <= M:
    print(m,M)
else:
    print(-1)