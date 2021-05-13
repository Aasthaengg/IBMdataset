import itertools
import functools
import math
from collections import Counter

N,X,Y=map(int,input().split())

k=[]

for i in range(1,N):
    for j in range(i+1,N+1):
        chk = min(abs(j-i),abs(X-i)+abs(j-Y)+1)
        k.append(chk)

a=Counter(k)

for i in range(1,N):
    print(a[i])
