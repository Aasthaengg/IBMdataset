n = int(input())
x = list(map(int, input().split()))

import numpy as np
ary = np.array(x)
ranks = ary.argsort()
rank_dict = {index:rank for rank,index in enumerate(ranks, start=1)}

MID=n//2
upper = x[ranks[MID]]
lower = x[ranks[MID-1]]
for i in range(n):
    rank = rank_dict[i]
    if rank <= MID:
        print(upper)
    else:
        print(lower)