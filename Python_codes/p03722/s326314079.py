import sys
input = sys.stdin.readline
n,m=map(int,input().split())
to=[[]for _ in range(n)]
ot=[[]for _ in range(n)]
dic={}
for i in range(m):
    a,b,c=map(int,input().split())
    to[a-1].append([b-1,-c])
    ot[b-1].append([a-1,-c])
#print(to)
vi_to=[0]*n
vi_to[0]=1
from collections import deque
que=deque()
que.append(0)
while que:
    v=que.pop()
    for u,c in to[v]:
        if vi_to[u]:
            continue
        vi_to[u]=1
        que.appendleft(u)

vi_ot=[0]*n
vi_ot[n-1]=1
que=deque()
que.append(n-1)
while que:
    v=que.pop()
    for u,c in ot[v]:
        if vi_ot[u]:
            continue
        vi_ot[u]=1
        que.appendleft(u)

av=[0]*n
for i in range(n):
    if vi_to[i] and vi_ot[i]:
        av[i]=1
#print(av)

dist=[float("inf")]*n
dist[0]=0
for i in range(n):
    for a,toa in enumerate(to):
        for b,c in toa:
            if av[a] and av[b]:
                if dist[b]>dist[a]+c:
                    dist[b]=dist[a]+c
                    if i==n-1:
                        print("inf")
                        exit()
#print(dist)
print(-dist[n-1])
