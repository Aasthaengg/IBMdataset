import Queue
class Node:
    def __init__(self,v):
        self.v = v
        self.c = []

def bfs(n):
    d = {n.v:0}
    q = Queue.Queue()
    q.put(n)
    visited = set([n.v])
    while q.qsize() > 0:
        x = q.get()
        for c in x.c:
            if not c.v in visited:
                q.put(c)
                d[c.v] = d[x.v]+1
                visited.add(c.v)
    return d



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

d = bfs(nodes[1])
for nid in nodes:
    if not nid in d:
        d[nid] = -1
for k in d:
    print k,d[k]