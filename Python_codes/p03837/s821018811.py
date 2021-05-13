n, m = map(int, input().split())
abc = [list( map(int, input().split())) for _ in range(m)]

cost = [[] for _ in range(n)]
edges = dict()
for i in range(m):
    a = abc[i][0] - 1
    b = abc[i][1] - 1
    c = abc[i][2]
    cost[a].append((b, c))
    cost[b].append((a, c))

    edges[str(a) + ' ' + str(b)] = i
    edges[str(b) + ' ' + str(a)] = i

s = set()

# main
from heapq import heappop, heappush
for start in range(n):
    d = [float('inf') for i in range(n)] # 最短距離
    d[start] = 0

    q = [] # min-heap, (距離, 頂点)
    prev = [None] * n # 経路をたどるときに使う
    heappush(q, (d[start], start))
    while q:
        # print(q, d, prev)
        du, u = heappop(q) # 最短距離とその頂点
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            alt = du + weight
            if d[v] > alt:
                d[v] = alt
                prev[v] = u
                heappush(q, (alt, v))

    # print('最短距離: ', d)

    for goal in range(start + 1, n):
        goal = [goal]
        while prev[goal[-1]] != None:
            goal.append(prev[goal[-1]])
        goal = goal[::-1]

        for j in range(len(goal) - 1):
            edge_idx = edges[str(goal[j]) + ' ' + str(goal[j + 1])]
            s.add(edge_idx)

print(m - len(s))
