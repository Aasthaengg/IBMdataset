n = int(input())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
cl = list(map(int,input().split()))

al = sorted(al)
bl = sorted(bl)
cl = sorted(cl)

import bisect
bl_ac = []
for b in bl:
    idx = bisect.bisect_right(cl, b)
    bl_ac.append(n-idx)
import itertools
bl_ac = [0] + list(itertools.accumulate(bl_ac[::-1]))
bl_ac = bl_ac
ans = 0
for a in al:
    idx = bisect.bisect_right(bl, a)
    ans += bl_ac[n-idx]

print(ans)
