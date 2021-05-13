from collections import deque
n, q = map(int, input().split())

road = [[] for _ in range(n)]
cnt = [0 for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)

for i in range(q):
    idx, v = map(int, input().split())
    cnt[idx - 1] += v

dist = [-1] * n
que = deque()
dist[0] = 0
que.append(0)

while(len(que) != 0):
    # BFS/DFS
    v = que.pop()
    for r in road[v]:
        if dist[r] != -1:
            continue
        # print(r, v)
        dist[r] = dist[v] + 1
        cnt[r] += cnt[v]
        que.append(r)
print(*cnt)