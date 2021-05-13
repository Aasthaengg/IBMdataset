N,M = list(map(int,input().split()))
PY = []
for i in range(M):
    PY.append(list(map(int,input().split())))
    PY[-1].append(i)

PY_sorted = sorted(PY, key=lambda x: x[1])
PY_sorted2 = sorted(PY_sorted, key=lambda x: x[0])

PY = PY_sorted2
p = 0
y = 1
for i in range(M):
    if p != PY[i][0]:
        y = 1
    p = PY[i][0]
    identityString = str(PY[i][0]).zfill(6) + str(y).zfill(6)
    PY[i].append(identityString)
    y += 1

PY_sorted = sorted(PY, key=lambda x: x[2])

for i in range(M):
    print(PY_sorted[i][3])