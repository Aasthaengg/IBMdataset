n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

l = [[] for u in range(n + 1)]
for u, v in uv:
    l[u].append(v)

def bfs(v):
    q = [(x, 0) for x in list(v)]
    index = 0
    ret = set()
    while len(q) > index:
        x, step = q[index]
        index += 1
        if step == 3:
            ret.add(x)
            continue
        for y in l[x]:
            next = (y, step + 1)
            if next not in visited:
                visited.add(next)
                q.append(next)
    return ret

v = set([s])
visited = set([(s, 0)])
ret = 0
while True:
    v2 = bfs(v)
    if len(v2) == 0:
        ret = -1
        break
    ret += 1
    if t in v2:
        break
    v = v2

print(ret)