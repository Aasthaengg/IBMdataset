n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

counter = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    counter[p-1] += x

from collections import deque
que = deque([[0, counter[0]]])
visited = [0] * n
visited[0] = 1
while que:
    node, point = que.pop()
    for nn in G[node]:
        if visited[nn] == 1:
            continue
        visited[nn] = 1
        counter[nn] += point
        que.append([nn, counter[nn]]) 

print(*counter)
