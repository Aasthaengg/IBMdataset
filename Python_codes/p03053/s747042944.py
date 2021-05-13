from sys import stdin
import numpy as np
from numba import njit

@njit("i8(i8[:,:],i8,i8)",cache=True)
def search(grid,h,w):
    q=np.zeros(2*10**6+4,dtype=np.int64)
    now=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1:
                q[now]=i
                q[now+1]=j
                now+=2

    now,nex=0,now
    cnt=0
    while now!=nex:
        tmp=nex
        for i in range(now,nex,2):
            y=q[i]
            x=q[i+1]
            for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
                ny=y+dy
                nx=x+dx
                if 0<=ny<h and 0<=nx<w:
                    if grid[ny][nx]==0:
                        grid[ny][nx]=1
                        q[tmp]=ny
                        q[tmp+1]=nx
                        tmp+=2

        now,nex=nex,tmp
        cnt+=1

    return cnt-1

def main():
    #入力
    readline=stdin.readline
    h,w=map(int,readline().split())
    grid=[readline().strip() for _ in range(h)]
    grid=np.array([[1 if grid[i][j]=="#" else 0 for j in range(w)] for i in range(h)],dtype=np.int64)
    print(search(grid,h,w))

if __name__=="__main__":
    main()