n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

import bisect
ans=0
for mid in b:
    ind_t = bisect.bisect_left(a,mid)
    ind_b = bisect.bisect_right(c,mid)
    ans+=ind_t*(n-ind_b)

print(ans)