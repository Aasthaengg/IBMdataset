from collections import deque

n = int(input())
L = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    L[u-1].append((v-1, w))
    L[v-1].append((u-1, w))
d = [-1] * n
d[0] = 0
c = [0] * n
c[0] = 0
q = deque([0])
while q:
    t = q.popleft()
    dist = d[t]
    for v, w in L[t]:
        if d[v] < 0:
            d[v] = dist + w
            if d[v] % 2:
                c[v] = 1
            q.append(v)
for x in c:
    print(x)
