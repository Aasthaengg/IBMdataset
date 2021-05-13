N,M = map(int,input().split())
PY = [list(map(int,input().split())) for _ in range(M)]

dic = [[] for _ in range(N+1)]
for p,y in PY:
    dic[p].append(y)

for a in dic:
    a.sort()

dic2 = [{} for _ in range(N+1)]
for p in range(N+1):
    dic2[p] = {y:i+1 for i,y in enumerate(dic[p])}

for p,y in PY:
    y = dic2[p][y]
    print(str(p).zfill(6)+str(y).zfill(6))
