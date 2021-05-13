n, m = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(m)]

PY_sort = sorted(PY, key=lambda x: x[1])
PY_sort.sort(key=lambda x: x[0])

ID = {}
i, p = 1, PY_sort[0][0]
for v in PY_sort:
    if v[0] != p:
        i, p = 1, v[0]
    id = "%06d%06d"%(p, i)
    ID[v[1]] = id
    i += 1

for p, y in PY:
    print(ID[y])