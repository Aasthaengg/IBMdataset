a, b = map(int,input().split())
v = []
for _ in range(b):
    aa,bb = map(int, input().split())
    v.append([aa-1, bb-1])
res = 0
for i in range(b):
    visited = [False] * a
    curv = []
    for j in range(a):
        curv.append([])
    for j in range(b):
        if i == j:
            continue
        else:
            x, y = v[j]
            curv[x].append(y)
            curv[y].append(x)
    import collections
    q = collections.deque([])
    q.append(0)

    while len(q) > 0:
        curnode = q.pop()
        if visited[curnode] is True:
            continue

        visited[curnode] = True
        for j in range(len(curv[curnode])):
            nextnode = curv[curnode][j]
            if visited[nextnode] is False:
                q.append(nextnode)

    isbridge = False
    for j in range(a):
        if visited[j] is False:
            isbridge = True
    if isbridge:
        res += 1

print(res)
