N,X,Y = map(int,input().split())
g = [[] for _ in range(N+1)]
for i in range(1,N+1):
    if i != 1:
        g[i].append(i-1)
    if i != N:
        g[i].append(i+1)
g[X].append(Y)
g[Y].append(X)
from collections import deque
answer = [0]*(N+1)
for i in range(1,N+1):
    q = deque([i])
    d = [None]*(N+1)
    d[i] = 0
    while q:
        p = q.popleft()
        for j in g[p]:
            if d[j] == None:
                d[j] = d[p]+1
                q.append(j)
    for k in d[1:]:
        answer[k] += 1
for l in answer[1:-1]:
    print(l//2)