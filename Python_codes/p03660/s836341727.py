n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)
#print(g)

from collections import deque
q = deque()
visit = [-1]*n
q.append(0)
visit[0] = 0
while q:
    x = q.popleft()
    for new_x in g[x]:
        if visit[new_x] != -1:
            continue
        visit[new_x] = visit[x]+1
        q.append(new_x)
        #if new_x == n-1:
            #break
#print(visit)

q = deque()
visit2 = [-1]*n
q.append(n-1)
visit2[n-1] = 0
while q:
    x = q.popleft()
    for new_x in g[x]:
        if visit2[new_x] != -1:
            continue
        visit2[new_x] = visit2[x]+1
        q.append(new_x)
#print(visit2)

fe = 0
sn = 0
for i in range(n):
    if visit[i] <= visit2[i]:
        fe += 1
    else:
        sn += 1
if fe > sn:
    print('Fennec')
else:
    print('Snuke')
