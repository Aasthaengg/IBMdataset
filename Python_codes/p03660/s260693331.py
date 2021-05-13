from collections import deque

N = int(input())
edge = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)

distF = [-1]*N
distS = [-1]*N
def bfs(s,dist):
    q = deque([])
    q.append([s,0])
    while len(q) != 0:
        v = q.popleft()
        dist[v[0]] = v[1]
        for nv in edge[v[0]]:
            if dist[nv] != -1:
                continue

            dist[nv] = dist[v[0]] + 1
            q.append([nv,dist[nv]])

bfs(0,distF)
bfs(N-1,distS)
# print(distF)
# print(distS)
Fennec = 0
Snuke = 0
for i in range(N):
    if distF[i] <= distS[i]:
        Fennec += 1
    else:
        Snuke += 1
# print(Fennec)
# print(Snuke)
if Fennec > Snuke:
    print('Fennec')
else:
    print('Snuke')
