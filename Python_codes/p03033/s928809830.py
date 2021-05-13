import sys

n, q = map(int, input().split())
lines = sys.stdin.readlines()
coordinates = set()
kkk = []
for line in lines[:n]:
    s, t, x = map(int, line.split())
    sx = s - x
    tx = t - x
    kkk.append((x, sx, tx))
    coordinates.add(sx)
    coordinates.add(tx)
kkk.sort()
ddd = list(map(int, lines[n:]))
coordinates.update(ddd)
coordinates = {d: i for i, d in enumerate(sorted(coordinates))}
coord_len = len(coordinates)

ans = [-1] * coord_len
skip = [-1] * coord_len
for x, sx, tx in kkk:
    ss = coordinates[sx]
    tt = coordinates[tx]
    while ss < tt:
        sk = skip[ss]
        if sk == -1:
            ans[ss] = x
            skip[ss] = tt
            ss += 1
        else:
            ss = sk
print('\n'.join(map(str, map(ans.__getitem__, map(coordinates.get, ddd)))))
