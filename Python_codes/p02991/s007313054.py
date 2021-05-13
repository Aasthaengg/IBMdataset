from collections import  deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x : int(x) - 1, input().split())
    g[u].append(v)
s, t = map(lambda x : int(x) - 1, input().split())
d = [[-1, -1, -1] for _ in range(n)]

m = 0
p = 0
d[s][0] = 0

queue = deque([(s, 0)])
while queue:
    i, p0 = queue.popleft()
    p1 = (p0 + 1) % 3
    for j in g[i]:
        if d[j][p1] >= 0:
            continue
        d[j][p1] = d[i][p0] + 1
        if j == t and p1 == 0:
            print(d[j][p1] // 3)
            quit()
        queue.append((j, p1))
print(-1) 