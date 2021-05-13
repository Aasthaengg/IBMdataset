x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

bc = []
for bb in b:
    for cc in c:
        bc.append(bb + cc)
bc.sort()

from bisect import bisect_left, bisect_right

def C(x):
    # count "abc <= x"
    ret = 0
    for aa in a:
        idx = bisect_right(bc, x - aa)
        ret += idx
    return ret

kk = x * y * z - k + 1
lb = 0
ub = (10 ** 10) * 4
while ub - lb > 1:
    mid = (ub + lb) // 2
    if C(mid) >= kk:
        ub = mid
    else:
        lb = mid

kth = ub

l = []
for aa in a:
    idx = bisect_left(bc, kth - aa)
    for i in range(idx, len(bc)):
        l.append(aa + bc[i])

l.sort(reverse=True)
l = l[:k]
for ll in l:
    print(ll)
