N, Q = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(N-1):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

px = [0] * (N+1)

for i in range(Q):
    p, x = map(int, input().split())
    px[p] += x

v = [0] * (N+1)
q = [[1, 0]]

while q:
    x, parent = q.pop()
    v[x] += v[parent]
    v[x] += px[x]
    for y in graph[x]:
        if y == parent:
            continue
        q.append([y, x])

ans = [str(i) for i in v[1:]]
print(' '.join(ans))
