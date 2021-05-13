from operator import itemgetter
import bisect
from itertools import accumulate
N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
WV.sort(key=itemgetter(0, 1))
w, v = zip(*WV)
w0 = w[0]
w1 = w0 + 1
w2 = w1 + 1
w3 = w2 + 1
i0 = bisect.bisect_left(w, w0)
i1 = bisect.bisect_left(w, w1)
i2 = bisect.bisect_left(w, w2)
i3 = bisect.bisect_left(w, w3)
v0 = sorted(v[i0:i1], reverse=True)
v1 = sorted(v[i1:i2], reverse=True)
v2 = sorted(v[i2:i3], reverse=True)
v3 = sorted(v[i3:], reverse=True)
a0 = list(accumulate(v0)) + [0]
a1 = list(accumulate(v1)) + [0]
a2 = list(accumulate(v2)) + [0]
a3 = list(accumulate(v3)) + [0]
n0 = 1 + len(v0)
n1 = 1 + len(v1)
n2 = 1 + len(v2)
n3 = 1 + len(v3)

ans = 0
for i0 in range(n0):
    for i1 in range(n1):
        for i2 in range(n2):
            for i3 in range(n3):
                if i0*w0 + i1*w1 + i2*w2 + i3*w3 <= W:
                    ans = max(ans, a0[i0-1]+a1[i1-1]+a2[i2-1]+a3[i3-1])
print(ans)

