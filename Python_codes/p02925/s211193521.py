from collections import deque

def id(i, j):
    return v_id[min(i, j)][max(i, j)]

def TopologicalSort(graph, in_deg, N):
    sorted_v = []
    q = deque()

    for i in range(N):
        if in_deg[i] == 0:
            q.append(i)
    
    while q:
        v = q.popleft()
        for n_v in graph[v]:
            in_deg[n_v] -= 1
            if in_deg[n_v] == 0:
                q.append(n_v)
        
        sorted_v.append(v)

    if len(sorted_v) == N:
        return sorted_v
    else:
        return 0

N = int(input())
v_id = [[-1]*N for _ in range(N)]
graph = [[] for _ in range(N * (N - 1) // 2)]
in_deg = [0]*(N * (N - 1) // 2)

v = 0
for i in range(N):
    for j in range(N):
        if i < j:
            v_id[i][j] = v
            v += 1

for i in range(N):
    a = list(map(lambda x: int(x) - 1, input().split()))
    for j in range(N - 2):
        graph[id(i, a[j])].append(id(i, a[j + 1]))
        in_deg[id(i, a[j + 1])] += 1

sorted_v = TopologicalSort(graph, in_deg, N * (N - 1) // 2)

if not sorted_v:
    print(-1)
else:
    dist = [0]*(N * (N - 1) // 2)

    for v in sorted_v:
        for n_v in graph[v]:
            dist[n_v] = max(dist[n_v], dist[v] + 1)
    
    print(max(dist) + 1)