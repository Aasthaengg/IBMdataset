from collections import deque
N, Q = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x

que = deque([0])
parent = [-1]*N
while que:
    node = que.pop()
    for v in graph[node]:
        if v == parent[node]:
            continue
        parent[v] = node
        que.append(v)
        ans[v] += ans[node] 

print(*ans)
