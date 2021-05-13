from collections import defaultdict

n, m = map(int, input().split())
PY = [tuple(map(int, input().split())) for _ in range(m)]
sorted_PY = sorted(PY)
cnt = 1
now = sorted_PY[0][0]
d = defaultdict(int)
for p, y in sorted_PY:
    if now != p:
        cnt = 1
        now = p
    d[y] = (p, cnt)
    cnt += 1

for p, y in PY:
    l, r = map(str, d[y])
    if len(l) < 6:
        light = '0'*(6-len(l)) + str(l)
    else:
        light = str(l)
    if len(r) < 6:
        right = '0'*(6-len(r)) + str(r)
    else:
        right = str(r)
    print(light+right)
