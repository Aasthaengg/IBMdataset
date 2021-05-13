from collections import deque

n = int(input())
graph = {}
for i in range(1, n):
    a, b = map(int,input().split())
    try:
        if graph[a] is not None:
            graph[a].append(b)
    except:
        graph[a] = [b]
    try:
        if graph[b] is not None:
            graph[b].append(a)
    except:
        graph[b] = [a]
c = list(map(int, input().split()))
c.sort()
M = sum(c) - c[-1]
q = deque([1])
a = [0 for i in range(n)]
visited = []
while q:
    for x in list(q):
        visited.append(x)
        for y in graph[x]:
            if not y in visited:
                q.append(y)
        a[x-1] = str(c.pop())
        q.popleft()
print(M)
print(' '.join(a))