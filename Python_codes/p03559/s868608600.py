n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

import bisect
a.sort()
b.sort()
c.sort(reverse=True)
c = [-x for x in c]

ans = 0
for x in b:
    ans += bisect.bisect_left(a, x) * (bisect.bisect_left(c, -x))

print(ans)