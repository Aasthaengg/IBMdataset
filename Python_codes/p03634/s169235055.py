import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    a, b, c = a - 1, b - 1, c
    tree[a].append((b, c))
    tree[b].append((a, c))

limit = 100010
depth = [0] * limit

def dfs(v, p, d): # (現在の頂点v, vの親, 現在の距離)
    depth[v] = d
    for e in tree[v]:
        if e[0] == p: continue
        dfs(e[0], v, d + e[1])

q, k = map(int, input().split())
k -= 1
dfs(k, -1, 0)
for i in range(q):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    res = depth[x] + depth[y]
    print(res)