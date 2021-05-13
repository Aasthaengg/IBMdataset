import sys
sys.setrecursionlimit(10**9)

n = int(input())
edges = [[] for _ in range(n)]
costs = [-1]*n
def dfs(current):

    for nex, cost in edges[current]:
        if costs[nex] != -1:
            continue
        costs[nex] = costs[current] + cost
        dfs(nex)

for i in range(n-1):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

q, k = map(int, input().split())
k -= 1
costs[k] = 0
dfs(k)

res = []
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    res.append(costs[x]+costs[y])

for ans in res:
    print(ans)
