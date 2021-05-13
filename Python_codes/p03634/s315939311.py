# https://atcoder.jp/contests/abc070/tasks/abc070_d

# 都度のクエリーに答えていると時間が足りない。
# 必ずKを通過すると決まっているので、各頂点とKの距離を
# 事前に計算しておく。O(V + E)

from heapq import heappush, heappop
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((c, b))
    graph[b].append((c, a))
q, k = map(int, input().split())
queries = []
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    queries.append((x, y))


def dijkstra_with_heap(graph, start, v):
    distance = [float('infinity')] * v
    distance[start] = 0
    stack = [[0, start]] # cost, vertex
    while stack:
        _, vertex = heappop(stack)
        edges = graph[vertex]
        for d, t in edges:
            if d + distance[vertex] < distance[t]:
                distance[t] = d + distance[vertex]
                heappush(stack, (d, t))
    return distance


distance = dijkstra_with_heap(graph, k - 1, n)

for x, y in queries:
    ans = distance[x] + distance[y]
    print(ans)