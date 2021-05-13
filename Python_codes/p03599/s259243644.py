A, B, C, D, E, F = map(int, input().split())

water_masses = set()
for i in range(31):
    for j in range(31):
        mass = 100 * A * i + 100 * B * j
        if 0 < mass and mass <= F:
            water_masses.add(mass)

sugar_masses = set()
for i in range(3000 // C + C):
    for j in range(3000 // D + D):
        mass = C * i + D * j
        if mass <= F:
            sugar_masses.add(mass)

res_water = 100 * A
res_sugar = 0
for m_water in water_masses:
    for m_sugar in sugar_masses:
        if m_water + m_sugar > F:
            continue

        con = m_sugar / (m_water + m_sugar)
        if con <= (E / (100 + E)) and con > (res_sugar / (res_water + res_sugar)):
            res_water = m_water
            res_sugar = m_sugar


print(res_water + res_sugar, res_sugar)
