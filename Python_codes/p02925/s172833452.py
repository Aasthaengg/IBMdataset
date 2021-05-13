from collections import deque

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

M = N*(N-1)//2

for i in range(N):
    for j in range(N-1):
        p = min(i+1,A[i][j])
        q = max(i+1,A[i][j])
        match = M-(N-p+1)*(N-p)//2+q-p-1
        A[i][j] = match
        
graph = [[] for _ in range(M)]
indegree = [0 for _ in range(M)]

for i in range(N):
    for j in range(1,N-1):
        graph[A[i][j-1]].append(A[i][j])
        indegree[A[i][j]] += 1
        
dist = [None for _ in range(M)]
queue = deque([])

for k in range(M):
    if indegree[k]==0:
        dist[k] = 0
        queue.append(k)

cycle = False

while queue:
    node = queue.popleft()
    for adj in graph[node]:
        indegree[adj] -= 1
        dist[adj] = dist[node] + 1
        if indegree[adj]==0:
            queue.append(adj)
            
if any(indegree):
    cycle = True

print(-1 if cycle else max(dist)+1)