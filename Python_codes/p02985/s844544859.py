from collections import deque

mod = 10 ** 9 + 7

n, k = map(int, input().split())
es = tuple(set() for _ in range(n))
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    es[a].add(b)
    es[b].add(a)

ans = k

q = deque()

can_use = k - 1
# vに隣接する未着色の頂点を塗るのに使える色の数
# k色 - (親、自分)
for u in es[0]:
    ans = (ans * can_use) % mod
    can_use -= 1
    q.append((u, 0))

while q:
    v, pr = q.popleft()
    can_use = k - 2
    # vに隣接する未着色の頂点を塗るのに使える色の数
    # k色 - (親、自分)
    for u in es[v]:
        if u == pr:
            continue
        ans = (ans * can_use) % mod
        can_use -= 1
        q.append((u, v))

print(ans)
