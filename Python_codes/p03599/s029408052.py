a, b, c, d, e, f = list(map(int, input().rstrip().split()))
a *= 100
b *= 100

x, y = a, 0  
conc_best = 0

for i in range(f // a + 1):
    for j in range(((f - a * i) // b) + 1):
        water = i * a + j * b
        if water == 0:
            continue
        rest = f - water
        sug_max = e * water / 100
        for k in range(rest // c + 1):
            for l in range((rest - c * k) // d + 1):
                sugar = c * k + d * l
                conc = sugar / (sugar + water)

                if sugar <= sug_max and conc> conc_best:
                        conc_best = conc
                        x, y = sugar+water , sugar
print(x, y)