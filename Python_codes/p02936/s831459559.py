from collections import deque
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
count = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for j in range(Q):
    p, x = map(int, input().split())
    count[p-1] += x

que = deque([0])
flag = [False] * N

while que:
    v = que.pop()
    flag[v] = True
    for e in G[v]:
        if flag[e]:
            continue
        count[e] += count[v]
        que.appendleft(e)

print(*count)
