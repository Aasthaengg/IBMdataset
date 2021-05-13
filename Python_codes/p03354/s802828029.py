from collections import deque

n,m = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
XY = list(list(map(lambda x: int(x)-1, input().split())) for _ in range(m))
G = [[] for _ in range(n)]
for x, y in XY:
    G[x].append(y)
    G[y].append(x)

q = deque()
vis = [False]*(n)
ans = 0
for i in range(n):
    set_x, set_px = set(), set()
    q.append(i)
    while q:
        x = q.popleft()
        if vis[x]: continue
        vis[x] = True
        set_x.add(x)
        set_px.add(P[x])
        for y in G[x]:
            if vis[y]: continue
            q.append(y)
    ans += len(set_x & set_px)
print(ans)
