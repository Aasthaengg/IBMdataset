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
    H,W,D=map(int,input().split())
    A=[() for _ in range(H*W)]
    for i in range(H):
        a=list(map(int1,input().split()))
        for j,x in enumerate(a):
            A[x]=(i,j)
    c=[[0] for _ in range(D)]
    for i in range(D):
        for k,j in enumerate(range(i,H*W-D,D)):
            c[i].append(c[i][k]+abs(A[j][0]-A[j+D][0])+abs(A[j][1]-A[j+D][1]))
    Q=int(input())
    for _ in range(Q):
        L,R=map(int1,input().split())
        print(c[L%D][R//D]-c[L%D][L//D])

if __name__ == '__main__':
    main()
