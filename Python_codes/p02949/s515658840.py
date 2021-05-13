inf = float('inf')
V,E,P = map(int,input().split())
edge = []
edge_rev = []
for i in range(E):
    A,B,C = map(int,input().split())
    edge_rev.append([B-1,A-1,P-C])
    edge.append([A-1,B-1,P-C])

d = [inf]*V
d[0] = 0
for i in range(V):
    update = False
    for j in range(E):
        From,To,cost = edge[j]
        if d[From] != inf and d[To]>d[From]+cost:
            d[To]=d[From]+cost
            update = True
    if not update:
        break

d_rev = [inf]*V
d_rev[V-1] = 0
for i in range(V):
    update = False
    for j in range(E):
        From,To,cost = edge_rev[j]
        if d_rev[From] != inf and d_rev[To]>d_rev[From]+cost:
            d_rev[To]=d_rev[From]+cost
            update = True
    if not update:
        break

d_ = [x for x in d]
d_rev_ = [x for x in d_rev]



for j in range(E):
    From,To,cost = edge[j]
    if d[From] != inf and d_rev[From] != inf and d[To]>d[From]+cost:
        d[To]=d[From]+cost


for j in range(E):
    From,To,cost = edge_rev[j]
    if d[From] != inf and d_rev[From] != inf and d_rev[To]>d_rev[From]+cost:
        d_rev[To]=d_rev[From]+cost


loop = False
for i in range(V):
    if d[i] != 0 and d_rev[i] != 0:
        loop = (d[i]+d_rev[i] != d_[i]+d_rev_[i]) or loop

if loop:
    print(-1)

else:
    ans = -d[-1]
    print(max(0,ans))