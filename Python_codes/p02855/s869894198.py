h,w,k1=map(int,input().split())
s=[[1 if i=='#' else 0 for i in input()] for _ in range(h)]
from collections import deque
yoko=deque([])
for i in range(h):
    x=sum(s[i])
    if x>0:
        yoko.append([i, x])
k=0
lasty=0
while yoko:
    y=yoko.popleft()
    y0=y[0]
    if not yoko:
        y0=h-1
    lim=k+y[1]
    k+=1
    tmp=s[lasty:y0+1]+[]
    tmp = [list(x) for x in zip(*tmp)]
    for i in range(w):
        x=sum(tmp[i])
        if x>0:
            for j in range(y0+1-lasty):
                s[lasty+j][i]=k
            k+=1
            k=min(lim,k)
        else:
            for j in range(y0+1-lasty):
                s[lasty+j][i]=k
            k=min(lim,k)
    lasty=y0+1



for i in range(h):
    print(' '.join(map(str, s[i])))