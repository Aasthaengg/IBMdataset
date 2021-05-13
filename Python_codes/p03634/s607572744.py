from collections import defaultdict,deque
from sys import stdin,setrecursionlimit
import heapq,bisect,math,itertools,string,queue,copy
setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, stdin.readline().split()))

N= int(input())

#n:node s:start
dlines = defaultdict(set)
for i in range(N-1):
    x,y,cost = inpl()
    dlines[x].add((cost,y))
    dlines[y].add((cost,x))

Q,K = inpl()
query = []
for _ in range(Q):
    x2,y2 = inpl()
    query.append((x2,y2))


def dijkstra_heap(n,s,dlines):
    d = [10**20]*(n+1)
    used = [True]*(n+1)
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in dlines[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in dlines[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

res = dijkstra_heap(N,K,dlines)
for order in query:
    print(res[order[0]]+res[order[1]])
