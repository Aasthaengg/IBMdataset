from collections import Counter
H, W, M = list(map(int, input().split()))
h = [0]*M
w = [0]*M
for i in range(M):
    h[i], w[i] = list(map(int, input().split()))
hc = Counter(h)
wc = Counter(w)
hmax = max(hc.values())
wmax = max(wc.values())
lh = {k[0] for k in hc.items() if k[1] == hmax}
lw = {k[0] for k in wc.items() if k[1] == wmax}

ct = 0
for i in range(M):
    if h[i] in lh and w[i] in lw:
        ct += 1
if ct >= len(lh)*len(lw):
    print(hmax+wmax-1)
else:
    print(hmax+wmax)