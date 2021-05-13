from collections import deque
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
cnt = 0
for x in A:
    G = {i:[] for i in range(1,N+1)}
    for y in A:
        if y!=x:
            a,b = y
            G[a].append(b)
            G[b].append(a)
    hist = [0 for _ in range(N+1)]
    que = deque([1])
    hist[1] = 1
    while que:
        z = que.popleft()
        for w in G[z]:
            if hist[w]==0:
                que.append(w)
                hist[w]=1
    if sum(hist)<N:
        cnt += 1
print(cnt)