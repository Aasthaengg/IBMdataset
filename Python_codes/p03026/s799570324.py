from collections import deque

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)
c = list(map(int, input().split()))
c.sort()
m = sum(c[:-1])
ans = [-1] * n

q = deque([(0, -1)])
while q:
    v, pv = q.popleft()
    ans[v] = c.pop()
    for nv in g[v]:
        if nv == pv: continue
        q.append((nv, v))

print(m)
print(*ans)
