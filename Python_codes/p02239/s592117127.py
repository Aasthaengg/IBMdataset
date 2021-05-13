from collections import deque

n = int(input())
graph = [[0]]
for _ in range(n):
    u, k, *v = map(int, input().split())
    graph.append(v)

queue = deque([1])
ans = [-1 for _ in range(n + 1)]
ans[1] = 0
while queue:
    cur = queue.popleft()
    for next in graph[cur]:
        if ans[next] != -1:
            continue
        ans[next] = ans[cur] + 1
        queue.append(next)
for i in range(1, n + 1):
    print(i, ans[i])
