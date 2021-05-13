import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    H,W=map(int,input().split())
    A=[[] for _ in range(H+2)]
    A[0]=A[H+1]=['#']*(W+2)
    black=[]
    for i in range(1,H+1):
        row=list(input())
        A[i]=['#']+row+['#']
        for j,cell in enumerate(row):
            if cell=='#':
                black.append([i,j+1])
    nextcells=[]
    nextcells.extend(black)
    c=-1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    while nextcells:
        c+=1
        cells=[]
        cells.extend(nextcells)
        nextcells=[]
        for cell in cells:
            for k in range(4):
                if A[cell[0]+dy[k]][cell[1]+dx[k]]=='.':
                    nextcells.append([cell[0]+dy[k],cell[1]+dx[k]])
                    A[cell[0]+dy[k]][cell[1]+dx[k]]='#'
    print(c)
        

if __name__ == '__main__':
    main()
