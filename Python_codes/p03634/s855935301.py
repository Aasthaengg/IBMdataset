from collections import deque

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
q,k  = map(int,input().split())
dis = [float('inf')]*(n+1)
dis[k] = 0
que = deque(g[k])
while que:
    x,y  = que.popleft()
    if dis[x] == float('inf'):
        dis[x] = y
        for x_, y_ in g[x]:
            que.append((x_, dis[x]+y_))
    else:
        dis[x] = min(dis[x], y)

ans = []
for _ in range(q):
    x,y = map(int,input().split())
    ans.append(dis[x] + dis[y])
for a in ans:
    print(a)