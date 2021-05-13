N,M,P = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]

es = [[] for _ in range(N)]
bs = [[] for _ in range(N)]
for a,b,c in ABC:
    a,b = a-1,b-1
    es[a].append((b,c-P))
    bs[b].append((a,c-P))

go_set = set([0])
stack = [0]
while stack:
    v = stack.pop()
    for to,_ in es[v]:
        if to in go_set: continue
        go_set.add(to)
        stack.append(to)

bk_set = set([N-1])
stack = [N-1]
while stack:
    v = stack.pop()
    for to,_ in bs[v]:
        if to in bk_set: continue
        bk_set.add(to)
        stack.append(to)

use = go_set & bk_set
K = len(use)
INF = float('inf')
d = [INF] * N
d[0] = 0
for i in range(K):
    for v in range(N):
        if v not in use: continue
        for to,c in es[v]:
            if to not in use: continue
            if d[to] > d[v] - c:
                d[to] = d[v] - c
                if i==K-1:
                    print(-1)
                    exit()
print(max(0, -d[-1]))