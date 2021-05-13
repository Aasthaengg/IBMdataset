import sys
input = sys.stdin.readline
N,M,P = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]

es = [[] for _ in range(N)]
rs = [[] for _ in range(N)]
for a,b,c in ABC:
    a,b = a-1,b-1
    es[a].append(b)
    rs[b].append(a)

stack = [0]
vis_go = set([0])
while stack:
    v = stack.pop()
    for to in es[v]:
        if to in vis_go: continue
        vis_go.add(to)
        stack.append(to)
stack = [N-1]
vis_bk = set([N-1])
while stack:
    v = stack.pop()
    for to in rs[v]:
        if to in vis_bk: continue
        vis_bk.add(to)
        stack.append(to)
use = vis_go & vis_bk

INF = float('inf')
dist = [INF] * N
dist[0] = 0
for i in range(len(use)):
    for a,b,c in ABC:
        a,b,c = a-1,b-1,P-c
        if a not in use or b not in use: continue
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            if i==len(use)-1:
                print(-1)
                exit()
print(max(0,-dist[-1]))