from collections import deque
N, Q = map(int, input().split())
pathes = []
for _ in range(N-1):
    a, b = map(int, input().split())
    pathes.append((a, b))
childs = [[] for i in range(N+1)]
for a, b in pathes:
    childs[a].append(b)
    childs[b].append(a)
cnt = [0]*(N+1)
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p] += x
closed = [False]*(N+1)
nodes = deque()
nodes.append(1)
while len(nodes) != 0:
    node = nodes.popleft()
    closed[node] = True
    for c in childs[node]:
        if closed[c]:
            continue
        nodes.append(c)
        cnt[c] += cnt[node]
for i in range(1, N+1):
    print(cnt[i])