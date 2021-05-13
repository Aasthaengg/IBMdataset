import sys
input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n)]
edge = [{} for _ in range(n)]

for i in range(m):
    l, r, d = map(int, input().split())
    l, r  = l-1, r-1
    g[r].append(l)
    g[l].append(r)
    edge[l][r] = d
    edge[r][l] = -d

s = []
visit = [10**18]*n
for i in range(n):
    if visit[i] != 10**18:
        continue
    s.append(i)
    visit[i] = 0
    while s:
        v = s.pop()
        for u in g[v]:
            if visit[u] != 10**18:
                if visit[u] != visit[v]+edge[v][u]:
                    print('No')
                    exit()
            else:
                visit[u] = visit[v]+edge[v][u]
                s.append(u)
else:
    print('Yes')