n,k,q,*a=map(int,open(0).read().split())
import numpy as np
points=np.full(n,k)

for i in range(q):
    points-=1
    points[a[i]-1]+=1

for i in range(n):
    print('NYoe s'[points[i]>0::2])