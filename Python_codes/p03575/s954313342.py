import copy
from collections import deque

n , m = map(int,input().split())
route = [[] for i in range(n+1)]
nuku = []
for i in range(m):
    a , b = map(int,input().split())
    route[a].append(b)
    route[b].append(a)
    nuku.append([a,b])
ans = 0
for a , b in nuku:
    kari = copy.deepcopy(route)
    kari[a].remove(b)
    kari[b].remove(a)
    d = deque()
    d.append(1)
    tansaku = [True for i in range(n+1)]
    cou = 0
    tansaku[1] = False
    while d:
        cou += 1
        now = d.popleft()
        for k in kari[now]:
            if tansaku[k]:
                tansaku[k] = False
                d.append(k)
    if cou != n:
        ans += 1
print(ans)