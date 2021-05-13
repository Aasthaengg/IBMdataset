n = int(input())
a = sorted(list(map(int, input().split())))

import bisect

mid = (a[-1]+1)//2
mid_idx = bisect.bisect_left(a, mid)

if abs(mid - a[mid_idx-1]) <= abs(a[mid_idx] - mid):
    print(a[-1], a[mid_idx-1])
else:
    print(a[-1], a[mid_idx])