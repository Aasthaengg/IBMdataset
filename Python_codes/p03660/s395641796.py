from heapq import heappop, heappush
from collections import deque
n = int(input())
mp2 = []
route = [[] for i in range(n)]
for i in range(n-1):
    a , b = map(lambda x:int(x)-1,input().split())
    mp2.append((a,b,1))
    mp2.append((b,a,1))
    route[a].append(b)
    route[b].append(a)
inf=float('inf')
d=[inf for i in range(n)]
d[0]=0
prev=[None]*n
p=dict()
for i,j,k in mp2: p[i]=p.get(i,[])+[(j,k)]

q=[]
heappush(q,(d[0],0))
while q:
    du, u = heappop(q)
    if d[u]<du: continue
    for v,weight in p.get(u,[]):
        alt=du+weight
        if d[v]>alt:
            d[v]=alt
            prev[v]=u
            heappush(q, (alt,v))

p=[n-1]
while prev[p[-1]]!=None: p.append(prev[p[-1]])

p = p[::-1]
t = p[-(-len(p)//2)-1]

d = deque()
d.append(n-1)
visit = [False for i in range(n)]
siro = 1
visit[n-1] = True
visit[t] = True
while d:
    now = d.popleft()
    for i in route[now]:
        if not visit[i] and i != t:
            visit[i] = True
            d.append(i)
            siro += 1
kuro = n - siro
if kuro <= siro:
    print("Snuke")
elif kuro > siro:
    print("Fennec")
