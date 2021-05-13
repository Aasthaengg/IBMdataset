from collections import deque
n,m=map(int,input().split())
edge = [[] for i in range(n+1)]
#edge[i] : iから出る道の[行先]の配列
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
s,t = map(int, input().split())
queue = deque()
queue.append((s, 0))
visited = [[False] * 3 for _ in range(n+1)]
while queue:
    u, d = queue.popleft()
    if visited[u][d % 3]:
        continue
    visited[u][d % 3] = True
    if d % 3 == 0 and u == t:
        print(d // 3);exit()
    for v in edge[u]:
        queue.append((v, d+1))
print(-1)