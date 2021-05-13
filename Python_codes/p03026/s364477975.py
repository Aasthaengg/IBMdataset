*D, = open(0)
n = int(D[0])

edge = [[] for _ in range(n+1)]
v_val = [0 for _ in range(n+1)]

dist = {}

for i in range(1, n):
    a, b = map(int, D[i].split())
    edge[a].append(b)
    edge[b].append(a)
c = list(map(int, D[n].split()))
c = sorted(c, reverse=True)

from collections import deque
visited = [False for _ in range(len(edge))]
start = 1
que = deque()
que.append(start)
order = []
order.append(start)
visited[start] = True

while que:
    node = que.popleft()
    for it in edge[node]:
        if not visited[it]:
            order.append(it)
            visited[it] = True
            que.append(it)
# calculate cost
v_val = [0 for _ in range(len(c)+1)]
for i, it in enumerate(order):
    v_val[it] = c[i]

print(sum(c[1:]))
print(' '.join(map(str, v_val[1:])))