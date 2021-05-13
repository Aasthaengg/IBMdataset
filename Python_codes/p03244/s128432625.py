import itertools
from collections import Counter


n = int(input())
v = list(map(int, input().split()))
ev_cnt = Counter(v[::2])
od_cnt = Counter(v[1::2])
ev_cnt[-1] = 0
od_cnt[-2] = 0
ev = ev_cnt.most_common(2)
od = od_cnt.most_common(2)
ans = n
for (k1, v1), (k2, v2) in itertools.product(ev, od):
    if k1 == k2:
        continue
    x = (n - v1 - v2)
    ans = min(ans, x)
print(ans)
