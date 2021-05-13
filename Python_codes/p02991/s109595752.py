from collections import deque

n, m = map(int, input().split())

g = [[] * 1 for i in range(n*3)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a * 3 + 0].append(b * 3 + 1)
    g[a * 3 + 1].append(b * 3 + 2)
    g[a * 3 + 2].append(b * 3 + 0)


s, t = map(int, input().split())
s -= 1
t -= 1
d = [-1 for i in range(n*3)]
q = deque([])
q.append(s*3+0)
d[s*3+0] = 0
while q:
    v = q.popleft()
    for to in g[v]:
        if d[to] == -1:
            d[to] = d[v] + 1
            q.append(to)

if d[t*3+0] == -1:
    print(-1)
else:
    print(d[t*3+0] // 3)
