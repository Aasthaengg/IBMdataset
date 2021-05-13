import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M = map(int,readline().split())
UVST = list(map(int,read().split()))
S,T = UVST[-2:]
UV = UVST[:-2]; U = UV[::2]; V = UV[1::2]

graph = [[] for _ in range(1+N+N+N)]
for x,y in zip(U,V):
    x1=x+N; x2=x1+N
    y1=y+N; y2=y1+N
    graph[x].append(y1)
    graph[x1].append(y2)
    graph[x2].append(y)   

INF = 10**15
dist = [INF] * (N+N+N+1)
dist[S] = 0
q = [S]
while q:
    qq = []
    for x in q:
        for y in graph[x]:
            if dist[y] != INF:
                continue
            qq.append(y)
            dist[y] = dist[x] + 1
    q = qq

d = dist[T]

answer = -1 if d == INF else d//3
print(answer)