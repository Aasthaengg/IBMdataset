from collections import defaultdict, Counter, namedtuple, deque

NN = 202020
MOD = 10**9+7
INF = float("inf")

n, u, v = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(n-1)]
u -= 1
v -= 1
graph = [[] for _ in range(n)]
for a, b in Edge:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def bfs(start, player):
    que = deque([(start, -1, 0)])
    while que:
        node, par, dst = que.popleft()
        # print(node, par, dst)
        if len(graph[node]) == 1:
            # print(player, node)
            dst_dict[player][node] = dst

        for nxt in graph[node]:
            if nxt == par:
                continue
            que.append((nxt, node, dst+1))


dst_dict = [{}, {}]
bfs(u, 0)
bfs(v, 1)
# print(dst_dict[0], dst_dict[1])

max_time = 0
for k in dst_dict[0]:
    if dst_dict[0][k] < dst_dict[1][k]:
        max_time = max(max_time, dst_dict[1][k]-1)

print(max_time)

