#import numpy as np
import math
from bisect import bisect

N, D, A = map(int, input().split())
xh = [list(map(int, input().split())) for _ in range(N)]
xh.sort(key=lambda x: x[0])
x = [i[0] for i in xh]
h = [i[1] for i in xh]
#h_int = np.ceil(h/A)

cnt=0
damage=[0]*(N+1)

for i in range(len(x)):
    damage[i] += damage[i-1]
    h[i] -= damage[i]
    if h[i]<=0: continue
    h_int =  math.ceil(h[i]/A)
    cnt+=h_int
    damage[i]+=h_int*A
    r=bisect(x,x[i]+2*D)
    #print(damage[i])
    damage[r]-= A*h_int
    

print(int(cnt))
