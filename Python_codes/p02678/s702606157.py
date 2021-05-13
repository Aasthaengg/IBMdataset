from collections import deque
n,m = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
arrow = [-1]*(n+1)
d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if arrow[i]!=-1:
            continue
        arrow[i] = v
        d.append(i)
    # print(dist)

print('Yes')
print(*arrow[2:], sep='\n')