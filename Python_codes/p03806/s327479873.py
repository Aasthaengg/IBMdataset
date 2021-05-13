from collections import defaultdict
from bisect import bisect_right
INF = float('inf')
N, Ma, Mb = map(int, input().split())
a, b, c = [None] * N, [None] * N, [None] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())
hN = N // 2
dic1 = defaultdict(lambda : INF)
for i in range(1 << hN):
    _a, _b, _c = 0, 0, 0
    for j in range(hN):
        if (i >> j) & 1:
            _a += a[j]
            _b += b[j]
            _c += c[j]
    if _c < dic1[(_a, _b)]:
        dic1[(_a, _b)] = _c
dic2 = defaultdict(lambda : INF)
for i in range(1 << (N - hN)):
    _a, _b, _c = 0, 0, 0
    for j in range(N - hN):
        if (i >> j) & 1:
            _a += a[hN+j]
            _b += b[hN+j]
            _c += c[hN+j]
    if _c < dic2[(_a, _b)]:
        dic2[(_a, _b)] = _c
ans = INF
for k in dic1:
    _a, _b = k
    v = dic1[k]
    for i in range(1, N+1):
        ans = min(ans, v + dic2[(Ma*i-_a,Mb*i-_b)])
ans = ans if ans < INF else -1
print(ans)