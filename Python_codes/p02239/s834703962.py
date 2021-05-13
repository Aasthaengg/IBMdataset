from collections import deque

n = int(input())
AL = [None for _ in range(n + 1)]
for i in range(1, n + 1):
    ukv = [int(x) for x in input().split()]
    AL[ukv[0]] = ukv[2:]

que = deque([1])
visited = [False] + [True] + [False] * (n - 1)
dist = [-1] + [0] + [-1] * (n - 1)
while que:
    u = que.popleft()
    for v in AL[u]:
        if visited[v]: continue
        dist[v] = dist[u] + 1
        visited[v] = True
        que.append(v)

for i in range(1, n + 1):
    print(i, dist[i])
