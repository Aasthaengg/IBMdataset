import sys,heapq
from collections import defaultdict
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False

def ddprint(x):
  if DBG:
    print(x)

n,t = inm()
a = inl()
heappair = []
hpair = defaultdict(int)
hcnt = defaultdict(int)
hcnt[a[0]] = 1
mn = a[0]
dif = 0
for i in range(1,n):
    z = a[i]
    hcnt[z] += 1
    if z<mn:
        mn = z
    if z-mn>=dif:
        if z-mn>dif:
            dif = z-mn
        e = (-dif,mn,z)
        if e not in hpair:
            hpair[e] = 1
            heapq.heappush(heappair,e)
cnt = 0
v = 1
while len(heappair)>0:
    mdif,mn,z = heapq.heappop(heappair)
    if v==1:
        v = mdif
    if v != mdif:
        break
    cnt += min(hcnt[mn],hcnt[z])
print(cnt) 
