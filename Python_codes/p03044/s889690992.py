import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict
def dfs(node_i, oe):
    if ans[node_i] != -1:
        return
    next_nodes = graph[node_i]
    ans[node_i] = oe
    for next_i, cost in next_nodes:
        dfs(next_i, (oe+cost)%2)
        

N = int(input())
ans = [-1 for i in range(N+1)]
graph = defaultdict(list)
for i in range(N-1):
    u, v, w = map(int, input().split())
    graph[u] += [(v, w)]
    graph[v] += [(u, w)]

dfs(1, 0)
for i in range(1, N+1):
    print(ans[i])