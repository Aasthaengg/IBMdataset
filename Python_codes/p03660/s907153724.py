from collections import deque
N = int(input())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dist = [0 for _ in range(N+1)]
que = deque([(1,0)])
hist = [0 for _ in range(N+1)]
hist[1] = 1
while que:
    x,d = que.popleft()
    for y in G[x]:
        if hist[y]==0:
            hist[y] = 1
            dist[y] = d+1
            que.append((y,d+1))
pa ={}
x = N
while x!=1:
    for y in G[x]:
        if dist[y]==dist[x]-1:
            pa[x] = y
            break
    x = pa[x]
ch = {}
x=N
while x!=1:
    y = pa[x]
    ch[y] = x
    x = y
if dist[N]%2==1:
    k = dist[N]//2
    cnt = 0
    x = 1
    y = N
    while cnt<k:
        x = ch[x]
        y = pa[y]
        cnt += 1
    G[x].remove(y)
    G[y].remove(x)
    hist = [0 for _ in range(N+1)]
    que = deque([1])
    hist[1] = 1
    while que:
        a = que.popleft()
        for b in G[a]:
            if hist[b]==0:
                hist[b]=1
                que.append(b)
    n1 = sum(hist)
    n2 = N-n1
    if n1>n2:
        print("Fennec")
    else:
        print("Snuke")
else:
    k = dist[N]//2
    cnt = 0
    x = 1
    while cnt<k:
        x = ch[x]
        cnt += 1
    y = ch[x]
    G[x].remove(y)
    G[y].remove(x)
    hist = [0 for _ in range(N+1)]
    que = deque([1])
    hist[1] = 1
    while que:
        a = que.popleft()
        for b in G[a]:
            if hist[b]==0:
                hist[b]=1
                que.append(b)
    n1 = sum(hist)
    n2 = N-n1
    if n1>n2:
        print("Fennec")
    else:
        print("Snuke")