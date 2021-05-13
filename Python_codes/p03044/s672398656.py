from collections import deque
n = int(input())
V = [[] for i in range(n+1)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    V[u].append([v,w])
    V[v].append([u,w])
q = deque([])
dis = [-1]*(n+1)
q.append(1)
dis[1] = 0
while q:
    x = q.popleft()
    for y,z in V[x]:
        if dis[y] == -1:
            q.append(y)
            dis[y] = dis[x] + z
for i in range(1,n+1):
    if dis[i]%2 == 0:
        print(0)
    else:
        print(1)