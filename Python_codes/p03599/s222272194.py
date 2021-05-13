A, B, C, D, E, F = map(int, input().split())
a = 100 * A
b = 100 * B
waters = set()
sugers = set()
for i in range(F // a + 1):
    ai = a * i
    f = F - ai
    for j in range(f // b + 1):
        g = ai + b * j
        if g <= F:
            waters.add(g)
for i in range(F // C + 1):
    ci = C * i
    f = F - ci
    for j in range(f // D + 1):
        g = ci + D * j
        if g <= F:
            sugers.add(g)

waters = sorted(waters)
sugers = sorted(sugers)

ans_sum = 100 * A
ans_sg = 0
concetration = 0
for w in waters:
    for s in sugers:
        g = w + s
        if g == 0 or g > F:
            break
        if s > w // 100 * E:
            break
        c = s / g
        if concetration < c:
            concetration = c
            ans_sum = g
            ans_sg = s
print(ans_sum, ans_sg)
