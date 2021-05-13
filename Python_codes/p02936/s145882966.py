from collections import deque
n,q = map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
    
X =[0]*n
for w in range(q):
    p,x = map(int,input().split())
    X[p-1]+=x
    
def bfs(u):
    queue = deque([u])
    d = [None]*n
    
    d[u] = 0
    while queue:
        v=queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v]+1
                X[i] += X[v]
                queue.append(i)
    return d

p = [None]*n
d = bfs(0)

print(*X)