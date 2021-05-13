N, M = map(int, input().split())
PY = [list(map(int, input().split())) + [i] for i in range(M)]

PY.sort(key=lambda x: (x[0], x[1]))

prev_p, i = PY[0][0], PY[0][2]
out = [None] * len(PY)
out[i] = str(prev_p).zfill(6) + str(1).zfill(6)

cnt = 1
for p, y, idx in PY[1:]:
    if p != prev_p:
        cnt = 0

    cnt += 1
    prev_p = p
    out[idx] = str(p).zfill(6) + str(cnt).zfill(6)


for x in out:
    print(x)
