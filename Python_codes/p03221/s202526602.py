N,M = list(map(int,input().split()))
PY = []
for i in range(M):
    PY.append(list(map(int,input().split())) + [i])

PY.sort(key=lambda x:x[1],reverse=False)

KEN = [0]*N
SHIs = []

for i in range(M):
    P = PY[i][0]
    ind = PY[i][2]
    KEN[P-1] += 1
    X = KEN[P-1]
    S = str(P).zfill(6) + str(X).zfill(6)
    SHIs.append([S,ind])

SHIs.sort(key=lambda x:x[1],reverse=False)
for s in SHIs:
    print(s[0])