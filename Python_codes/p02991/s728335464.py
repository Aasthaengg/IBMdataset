from collections import deque

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for u, v in X:
    graph[u].append(v)

INF = 10 ** 9 + 7
ctr = [[INF] * (N + 1) for _ in range(3)]
ctr[0][S] = 0
stack = deque()
stack.append((0, S))
while stack:
    i, u = stack.popleft()
    j = (i + 1) % 3
    for v in graph[u]:
        if ctr[j][v] > ctr[i][u] + 1:
            ctr[j][v] = ctr[i][u] + 1
            stack.append((j, v))
            
if ctr[0][T] < INF:
    print(ctr[0][T] // 3)
else:
    print(-1)
