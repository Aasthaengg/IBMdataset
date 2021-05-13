from collections import defaultdict, deque

N, M = map(int, input().split())
e = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    e[(a, 0)].append((b, 1))
    e[(a, 1)].append((b, 2))
    e[(a, 2)].append((b, 0))

S, T = map(int, input().split())

d = deque()
d.appendleft((S, 0))

inf = float('inf')
dist = defaultdict(lambda: inf)
dist[(S, 0)] = 0

while d:
    next_node = d.pop()
    for v in e[next_node]:
        if(dist[v] > dist[next_node] + 1):
            dist[v] = dist[next_node] + 1
            if(v == (T, 0)):
                break
            d.appendleft(v)

ans = dist[(T, 0)]
if(ans == inf):
    print(-1)
else:
    print(ans//3)

