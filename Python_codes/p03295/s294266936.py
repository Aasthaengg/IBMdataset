n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
r = n
ans = 0
for i in range(n):
    if i>=r:
        ans += 1
        r = n
    if not graph[i]:
        continue
    mi = min(graph[i])
    r = min(r, mi)
print(ans)