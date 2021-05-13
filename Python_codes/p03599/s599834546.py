a, b, c, d, e, f = map(int, input().split())
kouho = 0
jisho = {}
max_a = 30 // a
max_b = 30 // b
for i in range(max_a + 1):
    for j in range(max_b + 1):
        water = (a * i + b * j) * 100
        if water == 0:
            continue
        lim1 = e * (a * i + b * j)
        lim2 = f - water
        lim = min(lim1, lim2)
        max_c = lim // c
        max_d = lim // d
        for k in range(max_c + 1):
            for m in range(max_d + 1):
                sugar = k * c + m * d
                if sugar > lim:
                    continue
                satoumizu = water + sugar
                if satoumizu > f:
                    continue
                if sugar == 0:
                    continue

                noudo = 100 * sugar / satoumizu
                if noudo > kouho:
                    kouho = noudo
                    jisho[noudo] = (sugar, satoumizu)
if kouho == 0:
    print(100 * a, 0)
    exit()
ans2, ans1 = jisho[kouho]
print(ans1, ans2)
