

import numpy as np

n=int(input())
ans=0
for a_ in range(n):
    l,r=map(int,input().split())
    ans+=r-l+1
print(ans)