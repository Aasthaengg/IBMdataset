import sys
from collections import defaultdict

input = sys.stdin.readline

H, W, m = map(int, input().split())

hor = [0] * H
ver = [0] * W
f = defaultdict(int)
for _ in range(m):
    h, w = map(int, input().split())
    hor[h - 1] += 1
    ver[w - 1] += 1
    f[str(h - 1) + '|' + str(w - 1)] = 1

hmax = max(hor)
hs = [i for i, v in enumerate(hor) if v == hmax]
vmax = max(ver)
vs = [i for i, v in enumerate(ver) if v == vmax]


ans = hmax + vmax

if len(hs) * len(vs) > m:
    print(ans)
    exit()

for k1 in hs:
    for k2 in vs:
        if f[str(k1) + '|' + str(k2)] == 0:
            print(ans)
            exit()
print(ans - 1)
