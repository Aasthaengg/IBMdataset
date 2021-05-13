from collections import deque, defaultdict
N, X, Y = map(int, input().split())  # N個の頂点, XとYが繋がっている

graph = [[] for _ in range(N)]
for i in range(N-1):
    graph[i].append(i+1)
    graph[i+1].append(i)
X -= 1
Y -= 1
graph[X].append(Y)
graph[Y].append(X)
# print(graph)

# 最後に//2すれば良い
ans = defaultdict(int)
for i in range(N):
    q = deque()
    # 開始のノード
    q.append(i)
    visited = [False]*N
    visited[i] = True
    distant = [100000] * N
    distant[i] = 0
    while len(q):
        v = q.popleft()
        for e in graph[v]:
            if visited[e]:
                continue
            distant[e] = distant[v] + 1
            ans[distant[e]] += 1
            visited[e] = True
            q.append(e)
    # 始点iからの幅優先探索完了
# print(ans)
for i in range(1, N):
    print(ans[i]//2)
