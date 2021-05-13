import itertools

A, B, C, D, E, F = map(int, input().split())

water, sugar = set(), set()
for a, b in itertools.product(range(F // (100 * A) + 1),
                              range(F // (100 * B) + 1)):
    tmp = 100 * A * a + 100 * B * b
    if 0 < tmp <= F:
        water.add(tmp)

for c, d in itertools.product(range(F // C + 1),
                              range(F // D + 1)):
    tmp = C * c + D * d
    if tmp <= F:
        sugar.add(tmp)

conc_max = 0
ans_w, ans_s = 100 * A, 0
for w, s in itertools.product(water, sugar):
    if w + s > F or w // 100 * E < s:
        continue
    conc = 100 * s / (w + s)
    if conc > conc_max:
        conc_max = conc
        ans_w, ans_s = w + s, s
print(ans_w, ans_s)
