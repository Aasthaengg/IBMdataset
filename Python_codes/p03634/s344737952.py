import sys
input = sys.stdin.readline

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = [int(x) for x in input().split()]
    edge[a - 1].append([c, b - 1])
    edge[b - 1].append([c, a - 1])
q, k = [int(x) for x in input().split()]
# print(edge)
import heapq
def dijkstra(s):
    d = [float("inf")]*n
    used = [False]*n
    d[s] = 0
    used[s] = True
    queue = []
    for e in edge[s]:
        heapq.heappush(queue, e)
    while queue:
        # print(queue, d)
        cost, to = heapq.heappop(queue)
        if used[to]:
            continue
        d[to] = cost
        used[to] = True
        for e in edge[to]:
            # print(e)
            if used[e[1]]:
                continue
            heapq.heappush(queue, [d[to] + e[0], e[1]])
    return d

d = dijkstra(k - 1)
# print(d)
ans = []
for _ in range(q):
    x, y = [int(x) for x in input().split()]
    ans.append(d[x - 1] + d[y - 1])
for i in ans:
    print(i)
