import sys
n = int(input())
sys.setrecursionlimit(2*n)
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))
colors = [None]*n
colors[0] = 0
def DFS(node):
    for c_node, l in graph[node]:
        if colors[c_node] is not None:
            continue
        colors[c_node] = (l+colors[node])%2
        DFS(c_node)
DFS(0)
for i in colors:
    print(i)