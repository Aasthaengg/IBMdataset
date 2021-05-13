from collections import deque

n = int(input())
d = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    d[a].append((b, c))
    d[b].append((a, c))
q, k = map(int, input().split())
D = [-1] * (n + 1)
D[k] = 0
que = deque([k])
while que:
    t = que.popleft()
    dist = D[t]
    for l, c in d[t]:
        if D[l] < 0:
            D[l] = dist + c
            que.append(l)
for _ in range(q):
    x, y = map(int, input().split())
    print(D[x] + D[y])
