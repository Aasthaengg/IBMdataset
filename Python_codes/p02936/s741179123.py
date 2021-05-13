n,q = map(int,input().split())
V = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    V[a].append(b)
    V[b].append(a)
s = [0]*(n+1)
for j in range(q):
    p,x = map(int,input().split())
    s[p] += x
from collections import deque
q = deque([])
reach = [-1]*(n+1)
q.append(1)
reach[1] = 0
while q:
    x = q.popleft()
    for v in V[x]:
        if reach[v] == -1:
            reach[v] = 0
            s[v] += s[x]
            q.append(v)
for i in range(1,n+1):
    print(s[i],end="")
    print(" ",end="")
print("")