n,m = map(int, input().split())
P = [0]+list(map(int, input().split()))
XY = list(list(map(int, input().split())) for _ in range(m))
G = [[] for _ in range(n+1)]
for x, y in XY:
    G[x].append(y)
    G[y].append(x)

# print(n,m)
# print(P)
# print(XY)
# print(G)
# for i in range(len(G)):#########
#     print(i, G[i])###############

from collections import deque
q = deque()
vis = [False]*(n+1)
ans = 0
for i in range(1,len(G)):
    # print('i',i, 'G[i]',G[i])
    inc_x = set()
    inc_px = set()
    q.append(i)
    while q:
        # print(q)
        x = q.popleft()
        if vis[x]: continue
        vis[x] = True
        inc_x.add(x)
        inc_px.add(P[x])
        # print('x',x,'P[x]',P[x],'G[x]',G[x])
        for y in G[x]:
            # print('y',y)
            if vis[y]: continue
            q.append(y)
    # print('inc_x',inc_x)
    # print('inc_px',inc_px)
    # print('inc_x&inc_px',inc_x&inc_px)
    # print('len(inc_x&inc_px)',len(inc_x&inc_px))
    ans += len(inc_x & inc_px)

print(ans)
