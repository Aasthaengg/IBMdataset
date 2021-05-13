n = int(input())
al = list(map(int, input().split()))

als =list(sorted(al))
m = als[n-1]

import bisect
x = bisect.bisect(als,m/2)

if abs(m/2 - als[x-1]) > abs(m/2 - als[x]):
    print(m,als[x])
else:
    print(m,als[x-1])