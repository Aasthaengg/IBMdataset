def main():
    water_a, water_b, sugar_c, sugar_d, max_sugar, max_mass = map(int, input().split())
    op_a = 30 // water_a
    op_b = 30 // water_b
    op_c = 3000 // sugar_c
    max_concentration = [water_a * 100, 0]
    for times_a in range(op_a + 1):
        for times_b in range(op_b + 1):
            for times_c in range(op_c + 1):
                now_water = water_a * times_a + water_b * times_b
                now_sugar_lim = now_water * max_sugar
                now_water *= 100
                now_sugar = sugar_c * times_c
                now_mass = now_water + now_sugar
                if max_mass < now_mass or now_water == 0 or now_sugar_lim < now_sugar:
                    break
                add = (min(max_mass - now_mass, now_sugar_lim - now_sugar) // sugar_d) * sugar_d
                now_mass += add
                now_sugar += add
                if now_mass * max_concentration[1] < sum(max_concentration) * now_sugar and now_sugar <= now_sugar_lim:
                    max_concentration = [now_water, now_sugar]
    print(sum(max_concentration), max_concentration[1])


if __name__ == '__main__':
    main()
