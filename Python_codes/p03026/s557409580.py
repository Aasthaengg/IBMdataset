from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

c = list(map(int, input().split()))
c.sort()
score = sum(c)-c[-1]

for i in range(n):
    if len(graph[i]) == 1:
        next_v = deque([i])
        break
# dfs
ans = [-1]*n
while next_v:
    v = next_v.popleft()
    ans[v] = c.pop()
    for i in graph[v]:
        if ans[i] != -1:
            continue
        next_v.append(i)

print(score)
print(*ans, sep=" ")
