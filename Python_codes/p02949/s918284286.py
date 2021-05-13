N, M, P = map(int, input().split())
from collections import deque,defaultdict
edge1 = [[] for _ in range(N)]
edge2 = [[] for _ in range(N)]
for i in range(M):
    a,b,c= map(int, input().split())
    edge1[a-1].append([b-1,P-c])
    edge2[b-1].append([a-1,P-c])
edges1 = set()
d = deque([0])
visited1 = defaultdict(lambda: False)
while len(d):
    v = d.popleft()
    for u,w in edge1[v]:
        if visited1[w*10**8+v*10**4+u] == False:
            visited1[w*10**8+v*10**4+u] = True
            edges1.add(w*10**8+v*10**4+u)
            d.append(u)
edges2 = set()
d = deque([N-1])
visited2 = defaultdict(lambda: False)
while len(d):
    v = d.popleft()
    for u,w in edge2[v]:
        if visited2[w*10**8+u*10**4+v] == False:
            visited2[w*10**8+u*10**4+v] = True
            edges2.add(w*10**8+u*10**4+v)
            d.append(u)
new_edge = list(edges1&edges2)
d = [10**10]*N
d[0] = 0
n = 0
while True:
    n += 1
    update = False
    for e in new_edge:
        w = e//10**8
        v = e%10**8//10**4
        u = e%10**4
        if d[u]>d[v]+w:
            d[u] = d[v]+w
            update = True
    if update == False:
        break
    if n==N and update==True:
        print(-1)
        exit()
print(max(0,-d[-1]))