import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    l, r, d = [int(x) for x in input().split()]
    g[l - 1].append((r - 1, d))
    g[r - 1].append((l - 1, -d))

d = [None] * n
visited = [0] * n

for i in range(n):
    if visited[i] != 0:
        continue
    stack = [i]
    d[i] = 1
    while stack:
        u = stack.pop()
        visited[u] = 1
        for v, d_ in g[u] :
            if d[v] is None:
                d[v] = d[u] + d_
                stack.append(v)
            else:
                if d[v] != d[u] + d_ :
                    print("No")
                    sys.exit()
print("Yes")
