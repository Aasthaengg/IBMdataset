from itertools import accumulate
import numpy as np
N=int(input())
N-=1
L=[26**(i+1) for i in range(15)]
sL=list(accumulate(L))
result=[]
k=0
for i in range(15):
    if N+1<=sL[i] and N>=25:
        N-=sL[i-1]
        k=i
        break
for m in range(k):
    time=0
    while N>=L[k-m-1]:
        N-=L[k-m-1]
        time+=1
    result.append(chr(time+97))
result.append(chr(N+97))
print(''.join(result))