N,M,P = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]
es = [[] for _ in range(N)]
rs = [[] for _ in range(N)]
for a,b,c in ABC:
    a,b = a-1,b-1
    es[a].append((b,P-c))
    rs[b].append(a)

stack = [0]
govisit = set([0])
while stack:
    v = stack.pop()
    for to,_ in es[v]:
        if to in govisit: continue
        govisit.add(to)
        stack.append(to)

stack = [N-1]
backvisit = set([N-1])
while stack:
    v = stack.pop()
    for to in rs[v]:
        if to in backvisit: continue
        backvisit.add(to)
        stack.append(to)
use = govisit & backvisit

INF = float('inf')
dist = [INF] * N
dist[0] = 0
for i in range(N):
    for fr,e in enumerate(es):
        if fr not in use: continue
        for to,c in e:
            if to not in use: continue
            if dist[to] > dist[fr] + c:
                dist[to] = dist[fr] + c
                if i==N-1:
                    print(-1)
                    exit()
print(max(0,-dist[-1]))