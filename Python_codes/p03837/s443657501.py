import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,m = map(int, input().split())
from collections import defaultdict
ns = defaultdict(set)
es = []
for i in range(m):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add((c,v))
    ns[v].add((c,u))
    es.append((u,v,c))
    
def dijkstra(start):
    import heapq
    vals = [None] * n
    h = [(0, start)] # (距離, ノード番号)
    vals[start] = 0
    while h:
        val, u = heapq.heappop(h)
        for d, v in ns[u]:
            if vals[v] is None or vals[v]>val+d:
                vals[v] = val+d
                heapq.heappush(h, (vals[v], v))
    return vals
unused = [True]*m
for u in range(n):
    vals = dijkstra(u)
    for i,(a,b,c) in enumerate(es):
        if abs(vals[a]-vals[b])==c:
            unused[i] = False
ans = sum(unused)
print(ans)