from collections import deque

N,M = map(int,input().split())
G = [None] + [[] for i in range(N)]
dist = [None]+[-1]*N
ans = [None]+[10**6]*N

for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

deq = deque()

dist[1] = 0
deq.append(1)

while len(deq) != 0:
    v = deq.popleft()
    
    for i in G[v]:
        if dist[i] != -1:
            if dist[v]-dist[i] == 1:
                ans[v] = i
            continue
        dist[i] = dist[v]+1
        deq.append(i)

print("Yes")

for i in range(2,N+1):
    print(ans[i])