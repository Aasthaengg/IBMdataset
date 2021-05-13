# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    H,W=map(int,input().split())
    N=int(input())
    a=list(map(int,input().split()))
    c=[[0]*W for _ in range(H)]
    nv=[[()]*W for _ in range(H)]
    for i in range(H):
        if i%2==0:
            for j in range(W):
                if j<W-1:
                    nv[i][j]=(i,j+1)
                else:
                    nv[i][j]=(i+1,j)
        else:
            for j in range(W-1,-1,-1):
                if j>0:
                    nv[i][j]=(i,j-1)
                else:
                    nv[i][j]=(i+1,j)
    v=(0,0)
    for i,x in enumerate(a,1):
        for _ in range(x):
            c[v[0]][v[1]]=i
            v=nv[v[0]][v[1]]
    for a in c:
        print(*a)

if __name__ == '__main__':
    main()
