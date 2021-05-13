from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

S, T = map(int, input().split())
S -= 1
T -= 1

q = deque([(S, 0)])
visited = [[0]*3 for _ in range(N)]
visited[S][0] = 1

flg = True
res = -1
while q and flg:
    v = q.popleft()
    for n_v in graph[v[0]]:
        n_dist = v[1] + 1
        if n_v == T and n_dist % 3 == 0:
            res = n_dist // 3
            flg = False
            break
        if not visited[n_v][n_dist % 3]:
            visited[n_v][n_dist % 3] = 1
            q.append((n_v, n_dist))

print(res)