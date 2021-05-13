from collections import deque
n,u,v = map(int,input().split())
l = [[]for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
rl = [0 for i in range(n+1)]
d = deque()
d.append([l[u],u])
while len(d):
    l0,now = d.popleft()
    for i in l0:
        if i == u:
            continue
        elif rl[i] == 0:
            rl[i] = rl[now] + 1
            d.append([l[i],i])
rl2 = [0 for i in range(n+1)]
d = deque()
d.append([l[v],v])
while len(d):
    l0,now = d.popleft()
    for i in l0:
        if i == v:
            continue
        elif rl2[i] == 0:
            rl2[i] = rl2[now] + 1
            d.append([l[i],i])
dis = rl[v]
nl = []
for i in range(n+1):
    nl.append([rl2[i],i])
nl.sort(key=lambda x:x[0],reverse=True)
for i in range(n+1):
    if nl[i][0] > rl[nl[i][1]]:
        ans = nl[i][0]-1
        break
print(ans)