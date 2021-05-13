import itertools
from collections import Counter
N  = int(input())
V = [int(x) for x in input().split()]
ev_cnt = Counter(V[::2])
od_cnt = Counter(V[1::2])
# 1種のみ
ev_cnt[-1] = 0
od_cnt[-2] = 0
# 最頻値の上位２種のみ使用
ev = ev_cnt.most_common(2)
od = od_cnt.most_common(2)
ans = N
for (k1,v1), (k2,v2) in itertools.product(ev,od):
    if k1==k2:
        continue
    x = N - v1 - v2
    if ans > x:
        ans = x
print(ans)