from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
c = list(map(int, input().split()))
c.sort(reverse=True)
ans = [None]*n
ans[0] = c[0]
q = deque([0])
i = 1
while q:
    node = q.popleft()
    for c_node in graph[node]:
        if ans[c_node] is not None:
            continue
        ans[c_node] = c[i]
        i += 1
        q.append(c_node)
print(sum(c)-c[0])
print(*ans)