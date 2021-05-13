(N, M, _), *PY = [list(map(int, s.split())) + [i] for i, s in enumerate(open(0))]
prev_p = 0
city_cnt = 1
PY.sort()
for i in range(M):
    p, y, _ = PY[i]
    if p != prev_p:
        city_cnt = 1
        prev_p = p
    PY[i].append(str(p).zfill(6) + str(city_cnt).zfill(6))
    city_cnt += 1
PY.sort(key=lambda x: x[2])
[print(x[-1]) for x in PY]
