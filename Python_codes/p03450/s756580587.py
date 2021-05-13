import sys,queue,math,copy,itertools,bisect,collections,heapq
sys.setrecursionlimit(10**7)
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())

N,M = LI()
g = [[i,0] for i in range(N+1)]
g_num = [1 for i in range(N+1)]

def find(x,z):
    if g[x][0] == x: return x,z
    r,d = find(g[x][0],g[x][1])
    g[x] = [r,d]
    return g[x][0],g[x][1]+z

def union(x,y,d):
    if g_num[g[x][0]] < g_num[g[y][0]]:
        x,y = y,x; d = -d
    g_num[g[x][0]] += g_num[g[y][0]]
    g_num[g[y][0]] = 0
    g[g[y][0]][1] = g[x][1] + d - g[y][1]
    g[g[y][0]][0] = g[g[x][0]][0]


for _ in range(M):
    l,r,d = LI()

    if find(l,0)[0] == find(r,0)[0]:
        if g[l][1] + d != g[r][1]:
            print('No')
            exit(0)
    else:
        union(l,r,d)
print('Yes')
