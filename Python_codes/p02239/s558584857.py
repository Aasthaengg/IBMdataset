n = int(input())

adj = [None]
for i in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

isSearched = [None] + [False] * n

distance = [None] + [-1] * n

import collections

def bfs(u):
    isSearched[u] = True
    distance[u] = 0
    edge = collections.deque()
    edge.append(u)
    while edge:
        c_e = edge.popleft()
        for n_e in adj[c_e]:
            if not isSearched[n_e]:
                isSearched[n_e] = True
                distance[n_e] = distance[c_e] + 1
                edge.append(n_e)


bfs(1)

for i, x in enumerate(distance[1:], start=1):
    print(i, x)