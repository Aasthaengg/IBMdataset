
from collections import deque

N, M = map(int, input().split())
H = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for a, b in X:
    graph[a].append(b)
    graph[b].append(a)


ans = 0
for i in range(N):
    ans += all(H[i] > H[j - 1] for j in graph[i + 1])

print(ans)
