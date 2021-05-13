a, b, c, d, e, f = map(int, input().split())

limit_water = f * 100 / (100 + e)
limit_suger = f * e / (100 + e)


waters = []
sugars = []

for i in range(31):
    for j in range(31):
        water = 100 * a * i + 100 * b * j
        if water != 0 and water <= 3000:
            waters.append(water)

for i in range(1500):
    for j in range(1500):
        sugar = c * i + d * j
        sugars.append(sugar)

ans = []
max_density = 0.0

sugars = list(set(sugars))
sugars.sort()
waters = list(set(waters))
waters.sort()

for water in waters:
    for sugar in sugars:
        if sugar + water <= f and sugar <= (water * e / 100):
            density = sugar / (sugar + water)
            if density >= max_density:
                ans = [water + sugar, sugar]
                max_density = density

print(*ans)

