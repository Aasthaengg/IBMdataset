n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

import bisect
rui=[0]
sm=0
for mid in b:
    ind = bisect.bisect_left(c,mid+1)
    sm+= (n-ind)
    rui.append(sm)

ans=0
for top in a:
    ind = bisect.bisect_left(b,top+1)
    tmp = rui[-1] - rui[ind]
    ans+=tmp
print(ans)