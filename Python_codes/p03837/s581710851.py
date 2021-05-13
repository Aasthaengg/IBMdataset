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
    N,M=map(int,input().split())
    d=[[INF]*N for _ in range(N)]
    for _ in range(M):
        a,b,c=map(int1,input().split())
        c+=1
        d[a][b]=c
        d[b][a]=c
    d2=[d[i][:] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d2[i][j]=min(d2[i][j],d2[i][k]+d2[k][j])
    ans=0
    for i in range(N):
        for j in range(N):
            if d[i][j]!=INF and d[i][j]!=d2[i][j]:
                ans+=1
    print(ans//2)

if __name__ == '__main__':
    main()
