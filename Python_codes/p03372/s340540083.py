import sys
input = sys.stdin.readline
N,C=map(int,input().split())
x=[]
v=[0]
for i in range(N):
    xx,vv=map(int,input().split())
    x.append(xx)
    v.append(v[i]+vv)

cw=[0]
for i in range(N):
    cw.append(max(cw[i],v[i+1]-x[i]))

ccw=[0]
for i in range(N):
    ccw.append(max(ccw[i],v[N]-v[N-i-1]-(C-x[-i-1])))

cw_ccw=0
for i in range(N-1):
    cw_ccw=max(cw_ccw,v[i+1]-x[i]*2+ccw[N-i-1])

ccw_cw=0
for i in range(N-1):
    ccw_cw=max(ccw_cw,v[N]-v[N-i-1]-(C-x[-i-1])*2+cw[N-i-1])
#print(cw,ccw)
#print(list([cw_ccw,ccw_cw]))
print(max(cw+ccw+list([cw_ccw,ccw_cw])))
