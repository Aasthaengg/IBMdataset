X=int(input())

import math
P=[0,1]
X0=90
for i in range(1,361):
    X0+=X
    P[0]+=math.cos(X0/180*math.pi)
    P[1]+=math.sin(X0/180*math.pi)
    if abs(P[0])<1e-10 and abs(1-P[1])<1e-10:
        print(i)
        break