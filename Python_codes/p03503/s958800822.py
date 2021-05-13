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
    N=int(input())
    F=[]
    for _ in range(N):
        F.append(list(map(int,input().split())))
    P=[]
    for _ in range(N):
        P.append(list(map(int,input().split())))
    ans=-INF
    for i in range(1,2**10):
        tmp=0
        l=[0]*N
        for j in range(10):
            if (i>>j)&1:
                for k in range(N):
                    l[k]+=F[k][j]
        for k in range(N):
            tmp+=P[k][l[k]]
        ans=max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()
