import math
N=int(input())
l=[int(input())for i in range(5)]
if N<=min(l):
    print(5)
else:
    m=[0]*5
    for i in range(5):
        m[i]=math.ceil(N/l[i])
    print(5+max(m)-1)