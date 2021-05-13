#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
dt = []
for i in range(n):
    t,d = inm()
    dt.append((d,t))
dt.sort(reverse=True)
a = dt[:k] # oisisa max, ignore variety

vals = [z[0] for z in a]
dsum = sum(vals)
typs = set([z[1] for z in a])
ntyp = len(typs)
mx = dsum+ntyp**2 # satisfy for a

b = dt[k:]
h = {}
for d,t in b:
    if t in typs:
        continue
    elif t not in h:
        h[t] = d
    else:
        h[t] = max(h[t],d)
c = [h[t] for t in h]
c.sort(reverse=True)
# for types not in a, max oisisa

h = {}
for d,t in a:
    if t not in h:
        h[t] = d
    else:
        h[t] = max(h[t],d)
vals = []
for d,t in a:
    if t in h and d==h[t]:
        del h[t]
    else:
        vals.append(d)
vals.sort()
# oisisa list for second or below for each type

for i in range(min(len(vals),len(c))):
    dsum += c[i]-vals[i]
    ntyp += 1
    mx = max(mx,dsum+ntyp**2)
print(mx)
