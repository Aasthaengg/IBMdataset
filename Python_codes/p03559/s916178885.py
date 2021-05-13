import bisect
import numpy as np
N = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))
b_bisect = [bisect.bisect_left(a,one) for one in b]
b_cumsum = np.cumsum(b_bisect)
c_bisect = [bisect.bisect_left(b,one) for one in c]

ans = 0
for one in c_bisect:
    if one == 0:
        continue
    else:
        ans += b_cumsum[one-1]
print(ans)
