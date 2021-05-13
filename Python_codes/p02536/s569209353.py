
n,m = map(int, raw_input().split())

def g(u,parent):
    if parent[u]!= u:
        parent[u] = g(parent[u], parent)
    return parent[u]
parent = range(n+1)
for _ in range(m):
    u,v = map(int, raw_input().split())
    pu,pv = g(u,parent), g(v,parent)
    if pu!= pv:
        parent[pu] = pv

ans = 0
for u in range(1, n+1):
    if g(u,parent) == u:
        ans+=1
print ans -1