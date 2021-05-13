from collections import defaultdict, deque

N, M = map(int, input().split())
edges = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

go_to = [None] * N

q = deque()
q.append((0, -1))
is_visited = set()

while q:
    node, prev = q.popleft()
    if node in is_visited:
        continue
    is_visited.add(node)
    go_to[node] = prev + 1
    for dest in edges[node]:
        q.append((dest, node))

print('Yes')
for i in range(1, N):
    print(go_to[i])

