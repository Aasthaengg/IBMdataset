from collections import deque
n = int(input())
edge = []
dist = [-1]*(n+1)
for i in range(n+1):
    edge.append([])
for i in range(n-1):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))
q,k = map(int,input().split())
dist[k] = 0
que = deque([k])
used = set()
used.add(k)
while que:
    here = que.popleft()
    dist_here = dist[here]
    for i in edge[here]:
        if i[0] not in used:
            que.append(i[0])
            used.add(i[0])
            dist[i[0]] = dist_here + i[1]
for i in range(q):
    x,y = map(int,input().split())
    print(dist[x]+dist[y])




