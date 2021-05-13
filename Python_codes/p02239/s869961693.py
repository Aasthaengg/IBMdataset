from collections import deque
n = int(input())
u = []
k = []
v = []

for i in range(n):
    tmp = list(map(int, input().split()))
    u.append(tmp[0])
    k.append(tmp[1])
    if tmp[1] != 0:
        v.append(tmp[2:])
    else:
        v.append([])
        
d = deque([1])
dis = [-1]*n
dis[0] = 0
visit = [False]*n
visit[0] = True
while len(d) > 0:
    go = d[0]
    flag = False
    for i in v[go-1]:
        if not visit[i-1]:
            d.append(i)
            dis[i-1] = dis[go-1] + 1
            visit[i-1] = True
            flag = True
    d.popleft()
    
for i in range(n):
    print(i+1, dis[i])
