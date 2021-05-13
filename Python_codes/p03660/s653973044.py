import sys
input = sys.stdin.readline
n=int(input())
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
from collections import deque
que=deque()
que.append(0)
unvisited=[1]*n
unvisited[0]=0
lf=[0]*n
while que:
    v=que.pop()
    for u in g[v]:
        if unvisited[u]:
            lf[u]=lf[v]+1
            que.appendleft(u)
            unvisited[u]=0
que=deque()
que.append(n-1)
unvisited=[1]*n
unvisited[n-1]=0
ls=[0]*n
while que:
    v=que.pop()
    for u in g[v]:
        if unvisited[u]:
            ls[u]=ls[v]+1
            que.appendleft(u)
            unvisited[u]=0
f=0
for i in range(n):
    if lf[i]<=ls[i]:
        f+=1
if f>n-f:
    print("Fennec")
else:
    print("Snuke")
