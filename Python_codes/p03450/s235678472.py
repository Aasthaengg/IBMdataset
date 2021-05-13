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
    edge=[[] for _ in range(N)]
    redge=[[] for _ in range(N)]
    for _ in range(M):
        l,r,d=map(int1,input().split())
        d+=1
        edge[l].append((r,d))
        edge[r].append((l,-d))
    s=0
    D=[-INF]*N
    used=[False]*N
    while True:
        for s in range(s,N):
            if not used[s]:
                break
        else:
            break
        D[s]=0
        stack=[s]
        while stack:
            v=stack.pop()
            used[v]=True
            for nv,d in edge[v]:
                if D[nv]==-INF:
                    D[nv]=D[v]+d
                else:
                    if D[nv]!=D[v]+d:
                        print('No')
                        exit()
                if not used[nv]:
                    stack.append(nv)
    print('Yes')


if __name__ == '__main__':
    main()
