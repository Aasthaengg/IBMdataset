#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]
"""
n,k = ip()
x = [inp() for i in range(n)]
"""
import sys
sys.setrecursionlimit(10**6)
def dfs(u):
    global vis,graph
    vis.add(u)
    for i in graph[u]:
        if i not in vis:
            dfs(i)


n,m = ip()
graph = {i:[] for i in range(1,n+1)}
for i in range(m):
    a,b = ip()
    graph[a].append(b)
    graph[b].append(a)
vis = set()
ct = 0
for i in range(1,n+1):
    if i not in vis:
        dfs(i)
        ct += 1
print(ct-1)