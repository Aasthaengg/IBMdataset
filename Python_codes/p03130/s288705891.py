from collections import deque

n=4
m=3
g=[[] for _ in range(n)] 
for _ in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    
def bfs(u, g, n):
    u -= 1
    queue = deque([u])
    d = [-1] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is -1:
                d[i] = d[v] + 1
                queue.append(i)
    return d

d = bfs(1, g, n)
d.sort()
if d[-1]==3:
    print('YES')
else:
    print('NO')