import bisect

N, M = [int(i) for i in input().split()]

PY = []
PYd = {i:[] for i in range(1, N+1)}

for i in range(M):
    x, y = [int(i) for i in input().split()]
    PYd[x].append(y)
    PY.append((x,y))
    
for i in PYd.keys():
    PYd[i].sort()
    
for p,y in PY:
    str_p = str(p).zfill(6)
    index = str(bisect.bisect(PYd[p], y)).zfill(6)
    print(str_p+index)