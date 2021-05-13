from collections import deque
n , k = map(int,input().split())
kouho = []
for i in range(n-1):
    for j in range(i+1,n):
        kouho.append((i,j))
s = len(kouho)
now = 0
ke = []
for i in range(n-2):
    for j in range(i+1,n-1):
        ke.append((i,j))
if len(ke) < k:
    print(-1)
    exit()
kesu = set()    
for i in range(k):
    kesu.add(ke[i])

route = [[] for i in range(n)]
m = 0
for i in range(s):
    if not kouho[i] in kesu:
        m += 1
        u , v = kouho[i]
        route[u].append(v)
        route[v].append(u)

d = deque()
d.append(0)
cou = 1
visit = [False for i in range(n)]
visit[0] = True
while d:
    now = d.popleft()
    for i in route[now]:
        if not visit[i]:
            cou += 1
            visit[i] = True
            d.append(i)

if cou != n:
    print(-1)
    exit()

print(m)
for i in range(s):
    if not kouho[i] in kesu:
        x , y = kouho[i]
        print(str(x+1) + " " + str(y+1))