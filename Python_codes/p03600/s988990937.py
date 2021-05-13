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
    A=[list(map(int,input().split())) for _ in range(N)]
    f=[[True]*N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if A[i][j]>A[i][k]+A[k][j]:
                    print(-1)
                    exit()
                elif i!=k and j!=k and A[i][j]==A[i][k]+A[k][j]:
                    f[i][j]=False
    ans=0
    for i in range(N):
        for j in range(N):
            ans+=A[i][j]*f[i][j]
    print(ans//2)

if __name__ == '__main__':
    main()
