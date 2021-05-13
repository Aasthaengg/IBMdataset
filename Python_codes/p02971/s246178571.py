n = int(input())
a = [int(input()) for _ in range(n)]

asort = sorted(a)

import bisect
for i in range(n):
    if bisect.bisect_left(asort,a[i]) < n-1:
        print(asort[-1])
    elif bisect.bisect_left(asort,a[i]) == n-1:
        print(asort[-2])