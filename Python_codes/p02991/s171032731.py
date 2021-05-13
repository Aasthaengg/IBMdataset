from collections import  deque

class Graph(): #directed
    def __init__(self,n,edge):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.deg = [0 for _ in range(n)]
        for e in edge:
            self.graph[e[0]-1].append(e[1]-1)
            self.deg[e[1]-1] += 1

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(M)]
S,T = map(lambda x: int(x)-1 ,input().split())

g = Graph(N,edge)

stack = deque([(S,0)])
used = [[False]*3 for _ in range(N)]

while stack:
    node,depth = stack.popleft()
    if node == T and depth % 3 == 0:
        print(depth//3)
        break
    for adj in g.graph[node]:
        if not used[adj][(depth+1)%3]:
            used[adj][(depth+1)%3] = True
            stack.append((adj,depth+1))
else:
    print(-1)