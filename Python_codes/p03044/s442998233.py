from collections import deque

N = int(input())
e = [[] for i in range(N)]
for i in range(1, N):
    u, v, w = map(int, input().split())
    e[u-1].append((v-1, w))
    e[v-1].append((u-1, w))
l = [-1 for i in range(N)]

q = deque()
l[0] = 0
q.append(0)
while (q):
    u = q.pop()
    for v, w in e[u]:
        if l[v] >= 0:
            continue
        if w % 2 == 0:
            l[v] = l[u]
        else:
            l[v] = 1 - l[u]
        q.append(v)

for col in l:
    print(col)
