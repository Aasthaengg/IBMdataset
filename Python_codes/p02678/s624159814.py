from collections import deque
def bfs():
    visited=[-1]*n
    q=deque()
    start=1
    visited[start-1]=0
    q.append(start)
    while q:
        now=q.popleft()
        for next in graph[now-1]:
            if visited[next-1]==-1:
                q.append(next)
                visited[next-1]=now
    return visited[1:]

n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n)]
for v in p:
    graph[v[0]-1].append(v[1])
    graph[v[1]-1].append(v[0])  # 有向グラフなら消す

#print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

ans=bfs()
if -1 in ans:
    print('No')
else:
    print('Yes')
    for i in ans:
        print(i)