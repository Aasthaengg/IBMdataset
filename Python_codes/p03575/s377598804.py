from collections import deque
N, M = map(int, input().split())
#辺を取り除くことはabのセットとなっている要素から取り除くことと等価。頂点を消すのではない。
ab = [list(map(int, input().split())) for _ in range(M)]
c = 0
for i in range(M):
    G = [[] for _ in range(N)]
    for j in range(M):
        if i == j:
            continue
        a, b = ab[j][0], ab[j][1]
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    Q = deque()
    Q.append(0)
    d = [0] * N
    d[0] = 1
    while Q:
        q = Q.popleft()
        for g in G[q]:
            if d[g] == 0:
                d[g] = 1
                Q.append(g)
    if 0 in d:
        c += 1

print(c)
