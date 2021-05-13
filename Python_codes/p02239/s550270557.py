n = int(input())
graph = {}
d = [-1] * (n+1)
for i in range(n):
    t = list(map(int, input().split()))
    v = t[0]
    k = t[1]
    graph[v] = [t[i+2] for i in range(k)]

from queue import Queue

def bfs(s):
    d[s] = 0
    q=Queue()
    q.put(s)
    while not q.empty():
        v=q.get()
        for child in graph[v]:
            if d[child] != -1: continue
            d[child] = d[v] + 1
            q.put(child)
bfs(1)
for i in range(1, n+1):print(i,d[i])