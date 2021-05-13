from collections import defaultdict
H,W,M = map(int,input().split())
L=[]
bomb = defaultdict(lambda: 0)
for i in range(M):
    h,w = map(int,input().split())
    L.append([h-1,w-1])
    bomb[(h-1,w-1)] = 1

h = dict()
w = dict()

for i in range(M):
    val = L[i][0]
    if val in h:
        h[val] += 1
    else:
        h[val] = 1

for i in range(M):
    val = L[i][1]
    if val in w:
        w[val] += 1
    else:
        w[val] = 1

maxh = []
maxw = []
m=-1
for val in h:
    if h[val]>m:
        m = h[val]

for val in h:
    if m==h[val]:
        maxh.append(val)

ans = m
m=-1
for val in w:
    if w[val]>m:
        m=w[val]

for val in w:
    if m==w[val]:
        maxw.append(val)

ans += m
#print(maxh)
#print(maxw)
for mh in maxh:
    for mw in maxw:
        if bomb[(mh,mw)]==0:
            print(ans)
            exit()

print(ans-1)