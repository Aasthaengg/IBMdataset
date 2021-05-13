n, m = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]

from collections import defaultdict
g = defaultdict(list)
for x, y in xy:
    x, y = x - 1, y - 1
    g[x].append(y)
    g[y].append(x)

visited = [0] * n
ans = 0

for i in range(n):
    if visited[i] == 0:
        q = [i]
        visited[i] = 1
        s = set([i])
        while q:
            cur = q.pop()
            for target in g[cur]:
                if visited[target] == 0:
                    visited[target] = 1
                    q.append(target)
                    s.add(target)

        ps = set()
        for j in s:
            ps.add(p[j] - 1)

        intersect = s & ps
        ans += len(list(intersect))
print(ans)
