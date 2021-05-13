def main():
    a, b, c, d, e, f = map(int, input().split())

    maxConcentration = 0
    resSugarWater = 0
    resSugar = 0

    for i in range(31):
        for j in range((29 * a * i // b) + 1):
            water = (i * a + j * b) * 100
            possibleSugar = int(min(f - water, water * e / 100))
            for k in range((possibleSugar // c) + 1):
                for l in range(((possibleSugar - k * c) // d) + 1):
                    sugar = k * c + l * d

                    if water + sugar > f:
                        break

                    if water + sugar == 0:
                        continue

                    concentration = 100 * sugar / (water + sugar)

                    if concentration >= maxConcentration:
                        maxConcentration = concentration
                        resSugarWater = water + sugar
                        resSugar = sugar
    
    print(resSugarWater, resSugar)

if __name__ == '__main__':
    main()