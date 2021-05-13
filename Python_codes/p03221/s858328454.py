N, M = [int(i) for i in input().split()]
PY = []
for i in range(M):
    PY.append([int(i) for i in input().split()])

x = {}

for i in range(len(PY)):
    prefecture = PY[i][0]
    year = PY[i][1]

    if prefecture in x.keys():
        x[prefecture].append((year, i))
    else:
        x[prefecture] = [(year, i)]

for i in x:
    x[i] = sorted(x[i])



for i in x:
    for t in range(len(x[i])):
        PY[x[i][t][1]] = str(i).zfill(6) + str(t + 1).zfill(6)

for py in PY:
    print(py)