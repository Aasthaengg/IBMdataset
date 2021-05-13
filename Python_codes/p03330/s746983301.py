N,C=(int(i) for i in input().strip().split(" "))
D=[]
c=[]
for i in range(C):
    D.append([int(i) for i in input().strip().split(" ")])
for i in range(N):
    c.append([int(i) for i in input().strip().split(" ")])
from collections import defaultdict
d0=defaultdict(int)
d1=defaultdict(int)
d2=defaultdict(int)
d=[d0,d1,d2]
for i in range(N):
    for j in range(N):
        d[(i+j+2)%3][c[i][j]]+=1

from itertools import permutations
l=list(range(1,C+1))
k=permutations(l,3)
m=999999999999999999999999
for p in k:
    w=0
    a0,a1,a2=p
    for i in d[0].keys():
        w+=(D[i-1][a0-1]*(d[0][i]))
    for i in d[1].keys():
        w+=(D[i-1][a1-1]*(d[1][i]))
    for i in d[2].keys():
        w+=(D[i-1][a2-1]*(d[2][i]))
    if w<m:
        m=w
print(m)


