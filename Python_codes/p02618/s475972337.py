import numpy as np
from random import randint

D=int(input())
c=[int(i) for i in input().split()]
s=[]
for d in range(D):
    s.append([int(i) for i in input().split()])


v = [0]*D
last = [[0 for i in range(26)] for d in range(D)]
t=[0]*D

v_pre=0
for d in range(D):

    if d>=1:
        last[d] = last[d-1][:]
    
    # 初期化
    idx_best=0
    last[d][idx_best] = d+1
    v=v_pre + s[d][idx_best] - sum([c[j]*(d+1 - last[d][j]) for j in range(26)])

    for i in range(1, 26):
        v_tmp = v - s[d][idx_best] + c[idx_best]*(d+1 - last[d][idx_best]) + s[d][i] - c[i]*(d+1 - last[d][i])
        if v < v_tmp:
            v = v_tmp
            last[d][i] = d+1
            
            if d>=1:
                last[d][idx_best]=last[d-1][idx_best]
            else:
                last[d][idx_best]=0
            
            idx_best=i
    
    v_pre = v
    t[d]=idx_best + 1           # 1 <= t[d] <= 26 のため

for d in range(D):
    print(t[d])

v = [0]*D
for d in range(D):
    v[d] = s[d][t[d] - 1] - sum([c[i] for i in range(26)]) + c[t[d] - 1]

v_sum=0
for d in range(D):
    v_sum+=v[d]