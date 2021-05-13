H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

ans = [[-1] * W for _ in range(H)]

from itertools import cycle
v = cycle([(1,0),(0,1),(-1,0),(0,-1)])

def nextxy(x,y,nv):
    return x+nv[0],y+nv[1]

nv = next(v)
x,y = 0,0
for i,a in enumerate(A):
    while a > 0:
        ans[y][x] = i+1
        a -= 1
        nx, ny = nextxy(x,y,nv)
        if nx < 0 or W <= nx or ny < 0 or ny >= H or ans[ny][nx] != -1:
            nv = next(v)
        x, y = nextxy(x,y,nv)
        
for j in range(H):
    print(' '.join(map(str,ans[j])))
