from collections import deque
n = int(input())
g = [[] for i in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    a-=1; b-=1
    g[a].append(b)
    g[b].append(a)

def bfs(src):
    dist = [-1]*n
    dist[src] = 0
    dq = deque([src])
    while dq:
        now = dq.popleft()
        for to in g[now]:
            if dist[to]>=0: continue
            dist[to] = dist[now] + 1
            dq.append(to)
    return dist

df = bfs(0)
ds = bfs(n-1)

fscore = 0
sscore = 0
for f, s in zip(df, ds):
    if f <= s:
        fscore += 1
    else:
        sscore += 1
if fscore > sscore:
    print('Fennec')
else:
    print('Snuke')