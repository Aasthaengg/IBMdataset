N,C=map(int,input().split())
xv=[list(map(int,input().split())) for i in range(N)]
from itertools import accumulate
vc=list(accumulate([v for x,v in xv]))
vc=[vc[i]-x for i,(x,v) in enumerate(xv)]
va=list(accumulate([v for x,v in xv[::-1]]))
va=[va[i]-C+x for i,(x,v) in enumerate(xv[::-1])]
mc=[0]*N
for i in range(N):
    mc[i]=i if vc[mc[i-1]]<vc[i] else mc[i-1]
ma=[0]*N
for i in range(N):
    ma[i]=i if va[ma[i-1]]<va[i] else ma[i-1]
r=max(0,vc[mc[-1]])
for i in range(N-1):
    r=max(r,va[i]+vc[mc[-i-2]]-C+xv[-i-1][0])
r=max(r,va[ma[-1]])
for i in range(N-1):
    r=max(r,vc[i]+va[ma[-i-2]]-xv[i][0])
print(r)