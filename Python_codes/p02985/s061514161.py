from collections import deque
mod = 10**9 + 7
n, k = map(int, input().split())
edges = [[]*n for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

root = 0
d = deque([root])
visited = [False]*n
visited[root] = True
colored = [-1]*n
colored[root] = k
while d:
    p = d.pop()
    count = 0
    for c in edges[p]:
        if visited[c]:
            continue
        visited[c] = True
        d.append(c)
        if p == root:
            colored[c] = (k-1-count) % mod
        else:
            colored[c] = (k-2-count) % mod
        count += 1
ans = 1
for i in range(n):
    ans = ans*colored[i] % mod
print(ans)