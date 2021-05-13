from collections import deque

n, q = map(int, input().split())
eg = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)

cnt = [0] * (n + 1)
for i in range(q):
    p, x = map(int, input().split())
    cnt[p] += x


q = deque()
q.append(1)
seen = {1}
ans = [0] * (n + 1)
ans[1] = cnt[1]
while q:
    v = q.pop()
    for t in eg[v]:
        if t in seen:
            continue
        q.append(t)
        seen.add(t)
        ans[t] = ans[v] + cnt[t]

print(*ans[1:])
