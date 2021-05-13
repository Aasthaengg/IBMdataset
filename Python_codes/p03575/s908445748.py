import collections
def bfs(start):
    d = [-1]*n
    d[start] = 0
    q = collections.deque([start])
    while q:
        c = q.popleft()
        next_v = edge[c] 
        for v in next_v:
            if d[v] == -1:
                q.append(v)
                d[v] = d[c] + 1
    return d

n,m = map(int,input().split())
koho = []
edge = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    koho.append([a,b])
    edge[a].append(b)
    edge[b].append(a)
cnt = 0
for i in range(m):
    edge = [[] for _ in range(n)]
    for j in range(m):
        if i == j:
            continue
        edge[koho[j][0]].append(koho[j][1])
        edge[koho[j][1]].append(koho[j][0])
    a = bfs(0)
    flag = 0
    for j in a:
        if j == -1:
            flag = 1
    if flag == 1:
        cnt+=1
print(cnt)