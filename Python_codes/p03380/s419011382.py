n = int(input())
a = list(map(int, input().split()))
a.sort()

import bisect
import numpy as np
amax = a[-1]
cent = amax // 2

idx = bisect.bisect_left(a, cent)
if idx == len(a)-1:
    print(amax, a[-2])
else:
    max_idx = np.argmin([abs(a[idx]-cent), abs(a[idx-1]-cent)])
    if max_idx:
        print(amax, a[idx-1])
    else:
        print(amax, a[idx])
