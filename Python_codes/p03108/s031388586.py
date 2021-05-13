import sys, queue, math, copy, itertools, bisect, collections, heapq
LI = lambda: [int(x) for x in sys.stdin.readline().split()]
_LI = lambda: [int(x) - 1 for x in sys.stdin.readline().split()]
NI = lambda: int(sys.stdin.readline())

N, M = LI()
bridge = [_LI() for _ in range(M)]

g = [i for i in range(N)]
g_num = [1 for _ in range(N)]

def find(node):
    if g[node] == node: return node
    g[node] = find(g[node])
    return g[node]

def union(x,y):
#    if find(x) == find(y) : return
    if g_num[g[x]] > g_num[g[y]]: x,y = y,x
    g_num[g[y]] += g_num[g[x]]
    g[g[x]] = g[y]

benri = [0] * M
for i in range(M-1,-1,-1):
    x, y = bridge[i]
    if find(x) == find(y): continue
    benri[i] = g_num[g[x]] * g_num[g[y]]
    union(x,y)
ans = 0
for b in benri:
    ans += b
    print (ans)
