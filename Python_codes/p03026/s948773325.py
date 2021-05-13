from collections import deque
n = int(input())
g = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

c = [int(x) for x in input().split()]
c = sorted(c, reverse=True)

q = deque([0])
visited = [False]*n
ans = [-1]*n
ans[0] = c[0]
i = 1

while q:
    v = q.popleft()
    visited[v] = True
    for w in g[v]:
        if not visited[w]:
            ans[w] = c[i]
            i += 1
            q.append(w)

print(sum(c[1:]))
print(*ans)
