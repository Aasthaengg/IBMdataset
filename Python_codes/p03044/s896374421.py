import sys
sys.setrecursionlimit(20000000)

n = int(input())
G = [[] for _ in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append([v - 1, w])
    G[v - 1].append([u - 1, w])

def dfs(node, dist):
    for nxt_node, edge_size in G[node]:
        if ans[nxt_node] == -1:
            ans[nxt_node] = ((dist + edge_size) % 2)
            dfs(nxt_node, dist + edge_size)

ans = [-1] * n
dfs(0, 0)
print(*ans, sep='\n')
