import sys
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())

# グラフを作成(隣接リスト表現)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

# distance
dist = [-1] * (n + 1)
point = [-1] * (n + 1)
dist[0] = 0
dist[1] = 0
point[0] = 0
point[1] = 0

q = deque([])
q.append(1)

while len(q) > 0:
    v = q.popleft()
    # キューから先頭頂点(調べる点）を取り出す

    # v から辿れる頂点をすべて調べる
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        point[i] = v
        q.append(i)

if - 1 not in set(point):
    print('Yes')
    for k in point[2::]:
        print(k)
else:
    print('No')
