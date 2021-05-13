from collections import deque

n, m = map(int, input().split())
eg = [[] for _ in range(n + 1)]

al = [0] * m
bl = [0] * m

for i in range(m):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)
    al[i], bl[i] = a, b

ans = 0
for i in range(m):
    x, y = al[i], bl[i]
    q = deque()
    q.append(1)
    seen = {1}
    while len(q) > 0:
        v = q.pop()
        for t in eg[v]:
            if t in seen:
                continue
            elif (v == x and t == y) or (v == y and t == x):
                continue
            q.append(t)
            seen.add(t)
    if len(seen) != n:
        ans += 1
print(ans)
