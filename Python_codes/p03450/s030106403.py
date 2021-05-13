n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    g[l - 1].append((r - 1, d))
    g[r - 1].append((l - 1, -d))
l = [None] * n
for i in range(n):
    if l[i] != None:
        continue
    l[i] = 0
    stack = [i]
    while stack:
        d = stack.pop()
        for node, cost in g[d]:
            if l[node] == None:
                l[node] = l[d] + cost
                stack.append(node)
            else:
                if l[node] != l[d] + cost:
                    print('No')
                    exit(0)
print('Yes')
