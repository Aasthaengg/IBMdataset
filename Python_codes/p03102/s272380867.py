# その24
# ABC121 B - Can you solve this?

import numpy as np

n,m,c=map(int,input().split())
B = np.array(list(map(int,input().split())))
K=[]
for i in range(n):
    A = list(map(int,input().split()))
    K.append(A)

pp = np.array(K)
l = (pp*B).sum(axis=1)+c

t = 0
for i in range(len(l)):
    if l[i] > 0:
        t+=1
print(t)
