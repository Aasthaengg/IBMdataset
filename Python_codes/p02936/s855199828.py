n,q = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n-1)]
e = [list() for _ in range(n)]
for a,b in ab:
    e[a-1] += [b-1]
    e[b-1] += [a-1]
px = [list(map(int,input().split())) for _ in range(q)]
omomi = [0]*n
for p,x in px:
    omomi[p-1] += x

visited = [0]*n
visited[0] = 1
stack = [0]

while stack:
    v = stack.pop()
    for k in e[v]:
        if visited[k]==0:
            omomi[k] += omomi[v]
            visited[k] = 1
            stack.append(k)

print(*omomi)