# -*- coding: utf-8 -*-
import sys
import math
from queue import Queue
N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()
#%%
bound = [0]*N
idx = 0
right = 0
while idx<N:
    while right < N and (XH[right][0]-XH[idx][0])<=2*D:
        right += 1
    bound[idx] = right  
    idx += 1
def kiriage(n,m):
    return (n+(m-1))//m

heru = [0]*(N+1)
ans = 0
damage = 0
for i in range(N):
    damage -= heru[i]
    
    if XH[i][1]<=damage:
        continue
    cnt = kiriage(XH[i][1]-damage,A)
    ans += cnt
    damage += cnt*A
    heru[bound[i]] += cnt*A
print(ans)
            
        
        
