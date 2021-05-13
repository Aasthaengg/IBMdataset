n = int(input())
uvw = [0]*(n-1)
for i in range(n-1):
    uvw[i] = list(map(int,input().split()))
V = [[] for i in range(n+1)]
for u,v,w in uvw:
    V[u].append([v,w])
    V[v].append([u,w])
from collections import deque
q = deque([])
now = 1
reach = [0]*(n+1)
reach[now] = 2
q.append(now)
while q:
    x = q.popleft()
    for L in V[x]:
        if reach[L[0]] == 0:
            q.append(L[0])
            reach[L[0]] = reach[x] + L[1]
for A in reach[1:]:
    if A%2 == 0:
        print(0)
    else:
        print(1)