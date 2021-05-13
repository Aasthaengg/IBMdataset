from collections import deque

N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1

ans = [0] * (N + 1)

def push(q, dist, index, dist_v):
    if dist[index] != -1:
        return
    q.appendleft(index)
    dist[index] = dist_v

for i in range(N):
    q = deque()
    dist = [-1] * N
    push(q, dist, i, 0)
    while len(q) > 0:
        v = q.pop()
        d = dist[v]
        if v - 1 >= 0: push(q, dist, v - 1, d + 1)
        if v + 1 < N: push(q, dist, v + 1, d + 1)
        if v == X: push(q, dist, Y, d + 1)
        if v == Y: push(q, dist, X, d + 1)
    for j in range(N):
        ans[dist[j]] += 1

for i in range(N):
    ans[i] //= 2

for i in range(1, N):
    print(ans[i])
