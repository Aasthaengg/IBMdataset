N, M = map(int, input().split())
YP = [[] for _ in range(M)]
for i in range(M):
    p, y = map(int, input().split())
    YP[i] = [y, p, i]
    
YP = sorted(YP)

Num = [0 for _ in range(N+1)]
ID = []


for yp in YP:
    y = yp[0]
    p = yp[1]
    i = yp[2]
    
    Num[p] += 1
    id_p = str(p).zfill(6)
    id_c = str(Num[p]).zfill(6)
    ID.append([i, id_p + id_c])
ID = sorted(ID)
for id in ID:
    print(id[1])