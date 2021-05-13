from itertools import permutations
h, w = map(int, input().split())
c = []
for _ in range(10):
    c.append(list(map(int, input().split())))
a = [0]*10
for _ in range(h):
    for i in map(int, input().split()):
        if i<0:
            continue
        a[i] += 1
INF = 10**10
q = list(range(10))
dist = [INF]*10
dist[1] = 0
while q:
    mi = INF
    for i in q:
        if dist[i]<mi:
            mi = dist[i]
            mi_ind = i
    node = mi_ind
    q.remove(mi_ind)
    for i in range(10):
        if dist[node]+c[i][node] < dist[i]:
            dist[i] = dist[node]+c[i][node]

ans = 0
for i in range(10):
    ans += dist[i]*a[i]
print(ans)