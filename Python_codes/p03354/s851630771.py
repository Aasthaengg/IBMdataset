N, M = map(int, input().split())
p = list(map(int, input().split()))
g = [[] for _ in range(N)]

for xy in range(M):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

lst = []
visited = [0]*N
for i in range(N):
    if visited[i] == 1:continue
    temp = [i]
    grp = [i]
    visited[i] = 1
    while temp:
        q = temp.pop()
        for gq in g[q]:
            if visited[gq] == 0:
                temp.append(gq)
                visited[gq] = 1
                grp.append(gq)
    lst.append(grp)

ans = 0
for l in lst:
    temp = set([p[i]-1 for i in l])
    ans += len(temp & set(l))
print(ans)