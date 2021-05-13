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
    edge=[[] for _ in range(N)]
    for _ in range(N-1):
        a,b=map(int1,input().split())
        edge[a].append(b)
        edge[b].append(a)
    cost=[INF]*N
    cost[0]=0
    stack=[0]
    while stack:
        v=stack.pop()
        for nv in edge[v]:
            if cost[nv]==INF:
                cost[nv]=cost[v]+1
                stack.append(nv)
                if nv==N-1:
                    break
    d=cost[N-1]
    v=N-1
    for i in range(d+1):
        if i==(d-1)//2:
            sv=v
        elif i==(d+1)//2:
            fv=v
            break
        for nv in edge[v]:
            if cost[nv]==cost[v]-1:
                v=nv
                break

    stack=[sv]
    used=[False]*N
    used[fv]=True
    c=0
    while stack:
        v=stack.pop()
        used[v]=True
        c+=1
        for nv in edge[v]:
            if not used[nv]:
                stack.append(nv)
    if c>=N-c:
        print('Snuke')
    else:
        print('Fennec')
    

if __name__ == '__main__':
    main()
