n,m=map(int, input().split())
ab=[list(map(int, input().split())) for _ in range(m)]

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    flag=True
    for _i in range(n):
        if d[_i]==None:
            flag=False
    return flag

cnt=0
for i in range(m):
    graph = [[] for _ in range(n)]
    for j in range(m):
        if i!=j:
            graph[ab[j][0]-1].append(ab[j][1]-1)
            graph[ab[j][1]-1].append(ab[j][0]-1)
    if not bfs(0):
        cnt+=1
print(cnt)
