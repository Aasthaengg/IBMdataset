import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

def cond(x):
    s = 0
    for i in range(n):
        s += math.ceil(a[i]/x)-1
    return s <= k

l, r = 0, 10**9
while l+1 < r:
    mid = (l+r)//2
    if cond(mid):
        r = mid
    else:
        l = mid
print(r)