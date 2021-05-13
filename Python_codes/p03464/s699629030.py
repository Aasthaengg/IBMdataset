import math
K = int(input())
A = list(map(int, input().split()))
def check(init, A):
    cnt = init
    for a in A:
        group = cnt // a
        cnt = group * a
    return cnt

l,r = 0, 2**100
while r-l > 1:
    mid = (l+r)//2
    if check(mid, A) > 2:
        r = mid
    else:
        l = mid
maxcnt = l

l,r = 0, 2**100
while r-l > 1:
    mid = (l+r)//2
    if check(mid, A) < 2:
        l = mid
    else:
        r = mid
mincnt = r


if check(mincnt, A) == check(maxcnt, A) == 2:
    print(mincnt, maxcnt)
else:
    print(-1)

