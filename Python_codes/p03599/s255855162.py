a, b, c, d, e, f = map(int, input().split())
kouho = []
for i in range(f // (100 * a) + 1):
    for j in range(f // (100 * b) + 1):
        water = 100 * (a * i + b * j)
        if water > f:
            break
        if water == 0:
            continue
        sugar_max = (a * i + b * j) * e
        for k in range(sugar_max // c + 1):
            for l in range(sugar_max // d + 1):
                sugar = c * k + d * l
                if water + sugar > f:
                    break
                if sugar > sugar_max:
                    break
                density = (sugar / (water + sugar), water + sugar, sugar)
                kouho.append(density)
kouho.sort(reverse=True)
print(kouho[0][1], kouho[0][2])
