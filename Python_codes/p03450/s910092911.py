import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

n, m =map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    l, r, d = map(int, input().split())
    l, r = l-1, r-1
    g[l].append((d, r))
    g[r].append((-d, l))

s = []
visit = [-1]*n
dist = [False]*n
for i in range(n):
    if visit[i] == -1:
        s.append(i)
        visit[i] = 0
        dist[i] = 0
        while s:
            v = s.pop()
            for d, u in g[v]:
                if dist[u]:
                    if dist[u] != dist[v]+d:
                        print('No')
                        exit()
                if visit[u] == -1:
                    visit[u] = 0
                    dist[u] = dist[v]+d
                    s.append(u)
else:
    print('Yes')
