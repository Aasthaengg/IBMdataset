a, b, c, d, e, f = map(int, input().split())

set_ = set()
for i in range(3000):
    for j in range(3000):
        set_.add(c * i + d * j)

ans_noudo = -1
w = -1
s = -1
for i in range(31):
    for j in range(31):
        water = 100 * a * i + 100 * b * j
        if water == 0:
            continue
        if water > f:
            continue
        nokori = f - water
        for suger in range(0, nokori + 1):
            if suger not in set_:
                continue
            if water * e < suger * 100:
                continue
            noudo = 100 * suger / (water + suger)
            if ans_noudo < noudo:
                ans_noudo = noudo
                w = water
                s = suger
print(w + s, s)