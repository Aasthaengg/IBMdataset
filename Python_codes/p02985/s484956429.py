import sys
from collections import deque
read = sys.stdin.read
readline = sys.stdin.readline

N, K, *ab = map(int, read().split())
mod = 10 ** 9 + 7

graph = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(ab)] * 2):
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
checked = [False] * (N + 1)
checked[1] = True
answer = K
colors = K - 1

while queue:
    v = queue.popleft()
    for go in graph[v]:
        if not checked[go]:
            checked[go] = True
            answer *= colors
            answer %= mod
            queue.append(go)
            colors -= 1
    colors = K - 2

print(answer)