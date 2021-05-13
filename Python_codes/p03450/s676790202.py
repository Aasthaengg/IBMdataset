from collections import defaultdict


n, m = map(int, input().split())

edges = defaultdict(list)

for i in range(m):
    l, r, d = map(int, input().split())
    edges[l-1].append([r-1, d])
    edges[r-1].append([l-1, -d])

seen = [float('INF')] * n

for start in range(n):
    if seen[start] != float('INF'):
        continue

    seen[start] = 0
    todo = []
    while edges[start]:
        to, dist = edges[start].pop()
        seen[to] = dist
        todo.append([to, dist])

    while todo:
        node, dist = todo.pop()

        while edges[node]:
            to, add_dis = edges[node].pop()

            if seen[to] == float('INF') or seen[to] == dist+add_dis:
                seen[to] = dist + add_dis
                todo.append([to, dist+add_dis])

            else:
                print('No')
                exit()

print('Yes')