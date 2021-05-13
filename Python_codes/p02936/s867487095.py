from collections import deque

n, q = map(int,input().split())

edge = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

score = [0]*n

for i in range(q):
    p, x = map(int,input().split())
    score[p-1] += x

visited = [0]*n
visited[0] = 1

s = deque([0])
while s:
    now = s.pop()
    for v in edge[now]:
        if visited[v]:
            continue
        score[v] += score[now]
        visited[v] = 1
        s.append(v)

print(*score)