from collections import deque

n,x,y = map(int,input().split())

adj = [[] for i in range(n)]

adj[x-1].append(y-1)
adj[y-1].append(x-1)

for i in range(n-1):
    adj[i].append(i+1) 
    adj[i+1].append(i)
        
ans = [0 for _ in range(n)]

def bfs(start):
    inf = 1001001001
    q = deque()
    q.append(start)
    dist = [inf]*n
    dist[start] = 0
    
    while q:
        v = q.popleft()

        for i in adj[v]:
            if dist[i] == inf:
                dist[i] = dist[v] + 1
                q.append(i)

    for i in range(n):
        ans[dist[i]] += 1

for i in range(n):
    bfs(i)

for i in range(1,n):
    print(ans[i]//2)