from itertools import accumulate

n, x, *aa = map(int, open(0).read().split())

aa.sort()

aa = list(accumulate(aa))

ans = len([a for a in aa if a<=x])
if ans >= 1 and aa[-1]<x:
    ans -=1

print(ans)