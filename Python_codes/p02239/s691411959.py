from collections import deque
n = int(input())
grap = [[]]
for i in range(n):
    u,k,*v = map(int,input().split())
    grap.append(v)

dis = [-1]*(n+1)
dis[0] = 0
dis[1] = 0

d = deque()
d.append(1)
while d:
    v = d.popleft()
    for i in grap[v]:
        if dis[i] != -1:
            continue
        dis[i] = dis[v] + 1
        d.append(i)

for i in range(1,n+1):
    print(i,dis[i])

