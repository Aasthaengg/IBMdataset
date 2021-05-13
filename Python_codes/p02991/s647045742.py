from collections import deque
from collections import defaultdict
n, m = map(int, input().split())

edges = defaultdict(lambda: [])
for i in range(m):
    u, v = map(int, input().split())
    u1, v1 = (0, u), (1, v)
    u2, v2 = (1, u), (2, v)
    u3, v3 = (2, u), (0, v)
    edges[u1].append(v1)
    edges[u2].append(v2)
    edges[u3].append(v3)
    #u1, v1 = (0, v), (1, u)
    #u2, v2 = (1, v), (2, u)
    #u3, v3 = (2, v), (0, u)
    #edges[u1].append(v1)
    #edges[u2].append(v2)
    #edges[u3].append(v3)

#print(edges)
s, t = map(int, input().split())
s = (0, s)
t = (0, t)
#print(edges)
dist = {}
dist[s] = 0
visiting = deque()
visiting.append(s)
while len(visiting) > 0:
    #print(visiting)
    v = visiting.popleft()
    # check neighbors of v
    neighbors = edges[v]
    for neighbor in neighbors:
        if neighbor in dist:
            continue
        visiting.append(neighbor)
        if neighbor in dist:
            dist[neighbor] = min([dist[neighbor], dist[v] + 1])
        else:
            dist[neighbor] = dist[v] + 1
        
#print(dist)
#print(dist)
if t not in dist:
    print(-1)
else:
    if dist[t] % 3 == 0:
        print(dist[t] // 3 )
    else:
        print(-1)
