N,M = map(int,input().split())
PY = [list(map(int,input().split())) + [i] for i in range(M)]

PY.sort()

pnow = PY[0][0]
c = 1

ans = [-1 for i in range(M)]

for i in range(M):
    if pnow != PY[i][0]:
        c = 1
        pnow = PY[i][0]
    ans[PY[i][2]] = str(PY[i][0]).zfill(6) + str(c).zfill(6)
    c += 1

print('\n'.join(ans))
