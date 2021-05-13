from collections import deque
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
    
def bfs(u):
    queue = deque([u])
    d = [None]*n
    
    d[u] = 0
    while queue:
        v=queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v]+1
                p[i] = v
                queue.append(i)
    return d

p = [None]*n
d = bfs(0)
if None in p[1:]:
    print('No')
else:
    print('Yes')
        
for q in range(1,n):
    print(int(p[q])+1)