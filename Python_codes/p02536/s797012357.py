from collections import deque
n,m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    a-=1
    b-=1
    G[b].append(a)
    G[a].append(b)

dist = [-1]*n
que = deque()
cnt = 0

for i in range(n):
    if dist[i]!=-1:
        continue
    dist[i]=0
    que.append(i)
    while len(que):
        v = que.pop()
        s = G[v]
        for j in s:
            if dist[j]!=-1:
                continue
            dist[j]=0
            que.append(j)
    cnt += 1

print(cnt-1)