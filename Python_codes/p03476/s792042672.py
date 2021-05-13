# 69

import itertools
import bisect

q = int(input())
lr_l = [[int(x) for x in input().split()] for y in range(q)]

n_max = max(itertools.chain.from_iterable(lr_l))

isp_l = [True] * (n_max+1)
isp_l[0] = False
isp_l[1] = False

for i in range(2, int(n_max ** 0.5 + 2)):
    if not isp_l[i]:
        continue
    for j in range(i * 2, n_max + 1, i):
        isp_l[j] = False

p_l = [int(x) for x in range(n_max+1) if isp_l[x]]

l_l = []
for i in range(len(p_l)):
    if (p_l[i]+1)//2 in p_l:
        l_l.append(p_l[i])

for i in range(q):
    _l,_r = lr_l[i]
    _s = bisect.bisect_left(l_l, _l)
    _e = bisect.bisect_right(l_l, _r)
    print(_e-_s)
