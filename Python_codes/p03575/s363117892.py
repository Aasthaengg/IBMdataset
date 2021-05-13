from collections import deque
n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a-1, b-1))
ans = 0
for i in range(m):
    graph = [[] for _ in range(n)]
    for j in range(m):
        if i==j:
            continue
        a, b = ab[j]
        graph[a].append(b)
        graph[b].append(a)
    q = deque([0])
    seen = [False]*n
    seen[0] = True
    while q:
        node = q.popleft()
        for child in graph[node]:
            if seen[child]:
                continue
            seen[child] = True
            q.append(child)
    if not all(seen):
        ans += 1
print(ans)