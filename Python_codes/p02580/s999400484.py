from collections import *
h, w, m = map(int, input().split())
mh = [0 for _ in range(h)]
mw = [0 for _ in range(w)]

z = []
for _ in range(m):
    x, y = map(int, input().split())
    z.append((x-1, y-1))
    mh[x-1] += 1
    mw[y-1] += 1

hc = Counter(mh)
wc= Counter(mw)
hm = max(mh)
wm= max(mw)

ans = hm + wm
tmp = 0
for x, y in z:
    if mh[x] + mw[y] == ans:
        tmp += 1

if tmp == hc[hm] * wc[wm]:
    print(ans - 1)
else:
    print(ans)
