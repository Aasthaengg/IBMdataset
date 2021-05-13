# AB = [list(map(int, input().split())) for i in range(3)]

paths = [[] for _ in range(4)]
for _ in range(3):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    paths[a].append(b)
    paths[b].append(a)

start = 0
for i in range(4):
    if len(paths[i]) == 1:
        start = i
        break

visited = {start}
def dfs(n):
    if len(paths[n]) >= 3:
        print('NO')
        exit()
    for p in paths[n]:
        if p in visited:
            continue
        visited.add(p)
        dfs(p)

dfs(start)

if len(visited) == 4:
    print('YES')
else:
    print('NO')