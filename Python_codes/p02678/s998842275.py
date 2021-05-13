from sys import stdin
from collections import deque
import numpy as np
class edge(object):
    def __init__(self, to, rev):
        self.to = to
        self.rev = rev
def add_edge(from_, to_, G):
    G[from_].append(edge(to_, len(G[to_])))
    G[to_].append(edge(from_, len(G[from_])-1))

def bfs(src, level, li, li_from):
    que = deque([src])
    level[src] = 0
    while len(que)!=0:
        v = que.popleft()
        for i in range(len(li[v])):
            e = li[v][i]
            if level[e.to]<0:
                level[e.to] = level[v]+1
                li_from[e.to] = v
                que.append(e.to)

n,m = map(int, input().split())
li = []
for i in range(n):
    li.append([])
for i in range(m):
    a, b = map(int,  stdin.readline().split())
    if a > b:
        a, b = b, a
    add_edge(a-1, b-1, li)


if len(li[0])==0:
    print("No")
else:
    print("Yes")
    level = np.full(n, -1, dtype=np.int)
    li_from = np.full(n, -1, dtype=np.int)
    bfs(0,level,li, li_from)
    for i in li_from:
        if i==-1:
            continue
        print(i+1)

