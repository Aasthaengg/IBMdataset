a, b, c, d, e, f = map(int, input().split())
water_set = set()
sugar_set = set()

for i in range(31):
    for j in range(31):
        w = 100 * (a * i + b * j)
        if w > f:
            continue
        water_set.add(w)

for i in range(3001):
    for j in range(3001):
        s = c * i + d * j
        if s > f:
            continue
        sugar_set.add(s)

concentration_lim = e / (100 + e)
concentration = -1
ans_w = 0
ans_s = 0
for s in sugar_set:
    for w in water_set:
        total = s + w
        if total == 0:
            continue
        x = s / total
        if total <= f and x <= concentration_lim and x > concentration:
            concentration = x
            ans_w = total
            ans_s = s

print(ans_w, ans_s)
