class Node:
    def __init__(self,v):
        self.v = v
        self.c = []

def dfs(n,f,d,t,visited):
    visited.add(n.v)
    f[n.v] = t
    t2 = t
    for c in sorted(n.c,key=lambda x:x.v):
        if not c.v in visited:
            t2 = dfs(c,f,d,t2+1,visited)
    d[n.v] = t2+1
    return t2+1

n = int(raw_input())
nodes = {}
for _ in range(n):
    entry = map(int,raw_input().split(' '))
    nid = entry[0]
    if not nid in nodes: nodes[nid] = Node(nid)
    k = entry[1]
    if k > 0:
        children = entry[2:]
        for c in children:
            if not c in nodes: nodes[c] = Node(c)
            nodes[nid].c.append(nodes[c])

f = {}
d = {}
visited = set()
t = dfs(nodes[1],f,d,1,visited)
while len(visited) < len(nodes):
    for nid in nodes:
        if not nid in visited:
            t = dfs(nodes[nid],f,d,t+1,visited)

for k in f:
    print k,f[k],d[k]