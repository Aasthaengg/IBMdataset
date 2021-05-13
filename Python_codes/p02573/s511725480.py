n, m = map(int, input().split())

V = [set() for _ in range(n)] # 隣接リスト
for a, b in [[*map(lambda x: int(x)-1, input().split())] for _ in range(m)]:
    V[a].add(b)
    V[b].add(a)

from collections import deque, Counter
G = [-1] * n # グループ色分け
for s in range(n): # BFS
    dq = deque([s])
    while dq:
        p = dq.popleft()
        if G[p] >= 0: continue
        G[p] = s # 色付け
        for c in V[p]: dq.append(c)

print(max(Counter(G).values())) # 最大メンバ数
