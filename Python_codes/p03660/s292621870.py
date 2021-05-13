from collections import deque

N = int(input())
L = [[] for i in range(N)]
for i in range(N-1) :
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    L[u].append(v)
    L[v].append(u)

da = [0]*N
db = [0]*N

qa = deque([0])
visited = [False]*N
visited[0] = True
while qa :
    u = qa.popleft()
    for v in L[u] :
        if not visited[v] :
            visited[v] = True
            da[v] = da[u] + 1
            qa.append(v)

qb = deque([N-1])
visited = [False]*N
visited[N-1] = True
while qb :
    u = qb.popleft()
    for v in L[u] :
        if not visited[v] :
            visited[v] = True
            db[v] = db[u] + 1
            qb.append(v)

c = sum(da[i] <= db[i] for i in range(N))
ans = "Fennec" if c > N-c else "Snuke"
print(ans)
