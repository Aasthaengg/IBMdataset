from collections import deque
n = int(input())
G = [[]for i in range(n)]
for i in range(n-1):
    a,b = map(lambda x: int(x) - 1,input().split())
    G[a].append(b)
    G[b].append(a)

dist_zero = [-1]*n
dist_zero[0] = 0
queue = deque()
queue.append(0)
while queue:
    now = queue.popleft()
    for to in G[now]:
        if dist_zero[to] == -1:
            dist_zero[to] = dist_zero[now] + 1
            queue.append(to)

dist_n = [-1]*n
dist_n[-1] = 0
queue = deque()
queue.append(-1)
while queue:
    now = queue.popleft()
    for to in G[now]:
        if dist_n[to] == -1:
            dist_n[to] = dist_n[now] + 1
            queue.append(to)

f = sum([(dist_zero[i]<=dist_n[i]) for i in range(n)])

print("Fennec" if 2*f > n else "Snuke")