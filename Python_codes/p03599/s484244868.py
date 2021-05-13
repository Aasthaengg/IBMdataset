def main():
    a, b, c, d, e, f = map(int, input().split())
    max_weight = f // 100
    best_water = a
    best_suger = 0
    best_density = 0
    is_ideal = False
    for water in range(a, max_weight + 1):
        max_a = water // a
        max_b = water // b
        is_exist = False

        for add_a in range(max_a):
            water_a = (add_a + 1) * a
            is_exist = water_a + (water - water_a) // b * b == water
            if is_exist:
                break

        if not is_exist:
            for add_b in range(max_b):
                water_b = (add_b + 1) * b
                is_exist = water_b + (water - water_b) // a * a == water
                if is_exist:
                    break

        if is_exist:
            max_suger = e * water
            remaining = min(f - water * 100, max_suger)
            max_c = remaining // c
            max_d = remaining // d

            for add_c in range(max_c):
                sugar_c = (add_c + 1) * c
                sugar = sugar_c + (remaining - sugar_c) // d * d
                density = sugar / (water + sugar)
                if density > best_density:
                    best_density = density
                    best_water = water
                    best_suger = sugar
                    is_ideal = sugar == max_suger
                    if is_ideal:
                        break

            if not is_ideal:
                for add_d in range(max_d):
                    sugar_d = (add_d + 1) * d
                    sugar = sugar_d + (remaining - sugar_d) // c * c
                    density = sugar / (water + sugar)
                    if density > best_density:
                        best_density = density
                        best_water = water
                        best_suger = sugar
                        is_ideal = sugar == max_suger
                        if is_ideal:
                            break
            if is_ideal:
                break

    print(f'{best_water * 100 + best_suger} {best_suger}')


if __name__ == '__main__':
    main()
