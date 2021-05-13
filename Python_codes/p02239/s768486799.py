from collections import deque
n = int(input())
edges = [[]] + [list(map(int, input().split())) for _ in range(n)]
inf = 10 ** 4
d = [inf for _ in range(n+1)]

que = deque()
d[1] = 0
que.append(1)
while que:
    cur = que.popleft()
    for to in edges[cur]:
        if d[to] == inf:
            d[to] = d[cur] + 1
            que.append(to)

for i in range(1, n+1):
    if d[i] == inf:
        d[i] = -1
    print(i, d[i])

