# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: print('Yes' if b else 'No')
YESNO=lambda b: print('YES' if b else 'NO')

def main():
    N=int(input())
    edge=[[] for _ in range(N)]
    for i in range(N):
        l=list(map(lambda x:int(x)-1,input().split()))
        edge[i]=l[2:]
    d=[INF]*N
    d[0]=0
    que=deque()
    que.append(0)
    while que:
        v=que.popleft()
        for nv in edge[v]:
            if d[nv]>d[v]+1:
                d[nv]=d[v]+1
                que.append(nv)
    for i in range(N):
        print(i+1,d[i] if d[i]!=INF else -1)

if __name__ == '__main__':
    main()

