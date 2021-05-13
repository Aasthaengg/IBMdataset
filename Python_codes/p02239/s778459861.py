from collections import deque

N = int(input())
E = [None] * (N+1)
for _ in range(N):
    u, k, *vs = list(map(int, input().split()))
    E[u] = vs

d = [-1] * (N+1)
d[1] = 0
q = deque([(1, 0)])
while q:
    v, c = q.popleft()
    for u in E[v]:
        if d[u] < 0:
            d[u] = c+1
            q.append((u, c+1))

for i in range(1, N+1):
    print(i, d[i])
