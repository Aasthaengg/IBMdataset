import heapq
n, m = map(int, input().split())
inf = 10 ** 10
edges = [[] for _ in range(n)]
for _ in range(m):
    l, r, d = map(int, input().split())
    edges[l-1].append((r-1, d))
    edges[r-1].append((l-1, -d))

dist = [inf for _ in range(n)]

def dfs(v):
    stack = [v]
    dist[v] = 0

    while stack:
        v = stack.pop()
        d = dist[v]
        for to, cost in edges[v]:
            if dist[to] != inf:
                if dist[to] != d + cost:
                    return False
            else:
                dist[to] = d + cost
                stack.append(to)

    return True

flg = True
for i in range(n):
    if dist[i] == inf:
        if dfs(i) == False:
            flg = False
            break

print('Yes' if flg else 'No')