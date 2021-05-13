# -*- coding: utf-8 -*-
n,a,b,c = list(map(int,input().split()))
l = [int(input()) for i in range(n)]

#a,b,cに使うベースの竹を選ぶ
from itertools import permutations,product
inf=float("inf")
min_mp = inf
for k in product(range(4),repeat=n):
    if 2 not in k or 1 not in k or 0 not in k:
        continue
    len_abc = [0,0,0]
    mp = - 30
    for i,v in enumerate(k):
        if v == 3:
            pass
        else:
            len_abc[v]+=l[i]
            mp += 10
    mp += (abs(a-len_abc[0])+abs(b-len_abc[1])+abs(c-len_abc[2]))
    min_mp = min(min_mp,mp)
print(min_mp)