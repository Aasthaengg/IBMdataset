from collections import deque
import collections
import math

h,w = map(int, input().split())
c = [list(input()) for i in range(h)]

def bfs():
    res=0
    for y in range(h):
        for x in range(w):
            if c[y][x]=='.':
                c[y][x]=math.inf
                res += 1
    c[0][0]=0
    que=deque([[0,0]])
    while que:
        y,x=que.popleft()
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny,nx=y+i,x+j
            if h > ny >= 0 and w > nx >= 0:
                dist=c[ny][nx]
                if dist!='#':
                    if dist>c[y][x]+1:
                        c[ny][nx]=c[y][x]+1
                        que.append([ny,nx])
            else:
                pass
    if c[h-1][w-1] ==math.inf:
        return (-1)
    else:
        return res - c[h-1][w-1] -1

print (bfs())