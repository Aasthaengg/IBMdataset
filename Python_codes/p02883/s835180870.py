import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
n,k=map(int,readline().split())
a=np.array(readline().split(),np.int64)
f=np.array(readline().split(),np.int64)
a.sort()
f.sort()
f=f[::-1]

s=-1
e=10**12
while s+1<e:
    mid=(s+e)//2
    if a.sum()- np.minimum(a,mid//f).sum() <=k:
        e=mid
    else:
        s=mid
print(e)