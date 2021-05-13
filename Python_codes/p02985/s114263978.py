n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

mod = 10 ** 9 + 7

from collections import defaultdict
g = defaultdict(set)
for a, b in ab:
    g[a-1].add(b-1)
    g[b-1].add(a-1)

ans = k
q = [0]
visited = set([0])

while q:
    cur = q.pop()

    if cur == 0:
        tmp = k - 1
    else:
        tmp = k - 2
    for target in g[cur]:
        if target not in visited:
            ans = (ans * tmp) % mod
            tmp -= 1

            q.append(target)
            visited.add(target)

print(ans)
