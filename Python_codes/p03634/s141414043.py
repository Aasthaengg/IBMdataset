from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
Q, K = map(int, input().split())
visited = [0] * N
visited[K - 1] = 1
q = deque([(K - 1, 0)])
while q:
    p, c = q.popleft()
    for dst, d in graph[p]:
        if not visited[dst]:
            visited[dst] = c + d
            q.append((dst, c + d))
for _ in range(Q):
    x, y = map(lambda n: int(n) - 1, input().split())
    print(visited[x] + visited[y])