n = int(input())
uvw = [list(map(int, input().split())) for _ in range(n - 1)]

from collections import defaultdict, deque
g = defaultdict(list)
for u, v, w in uvw:
    g[u-1].append((v - 1, w))
    g[v-1].append((u - 1, w))

ans = [-1] * n
ans[0] = 0
q = deque([0])

while q:
    cur = q.popleft()
    for target, w in g[cur]:
        if ans[target] == -1:
            if w % 2 == 0:
                ans[target] = ans[cur]
            else:
                ans[target] = 1 - ans[cur]
            q.append(target)

for a in ans:
    print(a)
