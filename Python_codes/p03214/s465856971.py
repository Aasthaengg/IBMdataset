# 2019/10/15

import numpy as np

n=int(input())
a=np.array(list(map(int,input().split())))
avg=np.mean(a)

ans=abs(a-avg)
min_a=10**9
idx=-1
for i,e in enumerate(ans):
    if min_a>e:
        min_a=e
        idx=i
print(idx)