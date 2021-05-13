import bisect
import math

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

ans = sum(a)
for i in range(m):
    tmp = a.pop()
    ans -= tmp
    cost = math.floor(tmp/2)
    ans += cost
    idx = bisect.bisect_left(a,cost)
    a.insert(idx,cost)

print(ans)
