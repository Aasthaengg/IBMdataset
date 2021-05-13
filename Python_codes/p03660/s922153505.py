from collections import deque
n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)



def bfs(x):
    dis = [float("INF")]*n
    q = deque([])
    dis[x] = 0
    q.append((x,-1))
    while q:
        now,bef = q.popleft()
        for nex in e[now]:
            if nex != bef:
                dis[nex] = dis[now]+1
                q.append((nex,now))
    return dis

dis1 = bfs(0)
dis2 = bfs(n-1)
count = 0
for i in range(n):
    if dis1[i] <= dis2[i]:
        count += 1
    else:
        count -= 1
if count > 0:
    print("Fennec")
else:
    print("Snuke")

