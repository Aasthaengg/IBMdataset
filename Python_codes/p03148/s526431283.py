mi = lambda: map(int, input().split())
n, k = mi()
sushis = [list(mi()) for _ in range(n)]
types = set()
sushis.sort(key = lambda x: x[1], reverse = True)
bp = tp = sp = 0
exts = []
for t, d in sushis[:k]:
    bp += d
    if t in types:
        exts += d,
    else:
        types.add(t)
        tp += 1
sp = bp+tp**2
for t, d in sushis[k:]:
    if not exts: break
    if t not in types:
        types.add(t)
        bp += d-exts.pop()
        tp += 1
        sp = max(sp, bp+tp**2)
print(sp)