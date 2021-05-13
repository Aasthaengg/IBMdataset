import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M,*UV,S,T = map(int,read().split())

it = iter(UV)
G = [[] for _ in range(1+N+N+N)]
for x, y in zip(it, it):
    x1=x+N; x2=x1+N;
    y1=y+N; y2=y1+N;
    G[x].append(y1)
    G[x1].append(y2)
    G[x2].append(y)

INF = 10 ** 15
dist = [INF] * (N+N+N+1)
dist[S] = 0
q = [S]
while q:
    qq = []
    for x in q:
        for y in G[x]:
            if dist[y] != INF:
                continue
            qq.append(y)
            dist[y] = dist[x] + 1
            if y == T:
                break
    q = qq

d = dist[T]

answer = -1 if d == INF else d//3
print(answer)

