from collections import Counter
import numpy as np
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
d=Counter(np.cumsum(a)%m)
ans=0
for v in d.values():
  ans+=v*(v-1)//2
print(ans)