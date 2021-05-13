# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
edge=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int1,input().split())
    edge[a].append(b)
    edge[b].append(a)
C=list(map(int,input().split()))
C.sort()
print(sum(C)-C[-1])
que=deque([0])
ans=[-1]*N
while que:
    v=que.popleft()
    ans[v]=C.pop()
    for nv in edge[v]:
        if ans[nv]==-1:
            que.append(nv)
print(*ans)