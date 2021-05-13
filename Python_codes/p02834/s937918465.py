"""
シミュレートしてみればわかるが、高橋君は青木君よりも自分の方が近いようなノードのうち、青木君から最も遠いノードに向かって逃げるのが最善手。
そのようなノードをXとおくと、青木君と高橋君が鉢合わせるノードはXの一つ手前のノードになる。
したがって、青木君が動かす手の数はXまでの手数-1となる。
"""
from collections import deque
N,u,v = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

takahashiDist = [None]*(N+1)
que = deque([(u,0)])
while que:
    n,step = que.popleft()
    takahashiDist[n] = step
    for nx in edges[n]:
        if takahashiDist[nx] == None:
            que.append((nx,step+1))


aokiDist = [None]*(N+1)
que = deque([(v,0)])
while que:
    n,step = que.popleft()
    aokiDist[n] = step
    for nx in edges[n]:
        if aokiDist[nx] == None:
            que.append((nx,step+1))
ans = 0
for i in range(1,N+1):
    if aokiDist[i] > takahashiDist[i]:
        ans = max(ans,aokiDist[i]-1)
print(ans)