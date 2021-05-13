#C
import numpy as np
from itertools import combinations
N, M, X=map(int,input().split())
Book = []
for i in range(N):
    Book.append(list(map(int,input().split())))
Comb=[]
for i in range(N+1):
    Comb+=combinations(Book,i)
Sums=[]
for i in Comb[1:]:
    Sum=np.sum(np.array(i),axis=0)
    if all([j >= X for j in Sum[1:]]):
        Sums.append(Sum[0])
if len(Sums)==0:
    print(-1)
else:
    print(sorted(Sums)[0])