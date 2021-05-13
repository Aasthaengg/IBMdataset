A, B, C, D, E, F = map(int, input().split())

weight = 100 * A
suger = 0
den = 0
for a in range(0, F + 1, 100 * A):
    for b in range(0, F - a + 1, 100 * B):
        w = a + b
        if w == 0:
            continue
        S = E * w // 100
        for c in range(0, S + 1, C):
            for d in range(0, S - c + 1, D):
                s = c + d
                if w > 0 and w + s <= F and w * E >= s * 100:
                    tden = s / w
                    if den < tden:
                        weight = s + w
                        suger = s
                        den = tden

print(weight, suger)
