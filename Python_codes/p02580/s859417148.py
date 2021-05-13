H, W, M = map(int, input().split())
boms = []
h, w = [0] * (H + 1), [0] * (W + 1)
for _ in range(M):
    h_, w_ = map(int, input().split())
    boms.append([h_, w_])
    h[h_] += 1
    w[w_] += 1

hmax = max(h)
wmax = max(w)

cnt = h.count(hmax) * w.count(wmax)
for hh, ww in boms:
    if hmax == h[hh] and wmax == w[ww]:
        cnt -= 1

print(hmax + wmax - (cnt == 0))
