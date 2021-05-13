N, M, *_PY = map(int, open(0).read().split())
PY = []

for i in range(M):
    PY.append([_PY[i*2],_PY[i*2+1], i+1])
    
now_p = 0

for py in sorted(PY):
    if py[0] != now_p:
        now_p = py[0]
        cnt = 1
    else:
        cnt += 1

    py.append(str(py[0]).zfill(6) + str(cnt).zfill(6))
    
for py in PY:
    print(py[3])