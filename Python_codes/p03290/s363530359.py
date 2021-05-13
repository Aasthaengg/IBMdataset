D, G = map(int, input().split())
probs = [tuple(map(int, input().split())) for _ in range(D)]
res = 10 ** 4
for i in range(1 << D):
    comps = []
    idx = -1
    for j in range(D):
        if (i >> j) & 1:
            comps.append(j)
        else:
            idx = j
    g = G
    tmp = 0
    for c in comps:
        g -= 100 * (c + 1) * probs[c][0] + probs[c][1]
        tmp += probs[c][0]
    if g <= 0:
        res = min(res, tmp)
        continue
    else:
        t = (g + 100 * (idx + 1) - 1) // (100 * (idx + 1))
        if t <= probs[idx][0]:
            tmp += t
            res = min(res, tmp)
print(res)
