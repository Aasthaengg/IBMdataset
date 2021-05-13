from collections import deque
n = int(input())
to = [[] for i in range(n)]
col = [0] + [-1] * (n - 1)

for i in range(n - 1):
    u, v, w = map(int, input().split())
    to[u - 1].append((v - 1, w % 2))
    to[v - 1].append((u - 1, w % 2))

search = deque([0])
while search:
    v = search.popleft()
    for nv, nw in to[v]:
        if col[nv] != -1:
            continue
        col[nv] = (col[v] + nw) % 2
        search.append(nv)
print(*col, sep='\n')