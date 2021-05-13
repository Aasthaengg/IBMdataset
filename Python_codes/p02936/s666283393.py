import sys
sys.setrecursionlimit(10 ** 7)

n,q = map(int,input().split())
ab = [list(map(int,input().split()))for _ in range(n-1)]
px = [list(map(int,input().split()))for _ in range(q)]

graph = [[] for _ in range(n+3)]
for a,b in ab:
    graph[a].append(b)
    graph[b].append(a)

value = [0]*(n+1)
for p,x in px:
    value[p] += x

def dfs(v,parent,add):
    value[v] += add
    for x in graph[v]:
        if x == parent:
            continue
        dfs(x,v,value[v])

dfs(1,0,0)
print(*value[1:],end="\t")
