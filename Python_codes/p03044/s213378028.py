n = int(input())
visited = [False] * (n + 1)
distance = [0] * (n + 1)
prev = [0] * (n + 1)

from collections import defaultdict, deque
d = defaultdict(list)

for _ in range(n-1):
    u,v,w = list(map(int, input().split()))
    d[u].append((v, w))
    d[v].append((u, w))

q = deque([1])
while q:
    node = q.popleft()
    visited[node] = True
    for next_node, next_dist in d[node]:
        if not visited[next_node]:
            q.append(next_node)
            # 距離を更新
            distance[next_node] = distance[node] + next_dist
    
# print(distance)
for dist in distance[1:]:
    print(dist%2)