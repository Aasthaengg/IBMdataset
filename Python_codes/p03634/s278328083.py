n = int(input())
import sys
sys.setrecursionlimit(10**8)
def D(now,pre,SUM):
    dist[now] = SUM
    for BC in G[now]:
        if BC[0] == pre:
            continue
        D(BC[0],now,SUM+BC[1])



G = [[] for _ in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b,c))
    G[b].append((a,c))
q,k = map(int,input().split())
# xから頂点kまでの最短経路を求めておいて、kからyまでの最短経路を求めておく
k -= 1
# ここで作っとく?
dist = [0] * n
D(k,-1,0)
for i in range(q):
    x,y = map(lambda m:int(m)-1, input().split())
    print(dist[x] + dist[y])
