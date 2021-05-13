from collections import defaultdict
N, M = map(int, input().split())

G = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    l = G.get(i, None)
    if l is None:
        print(0)
    else:
        print(len(l))
