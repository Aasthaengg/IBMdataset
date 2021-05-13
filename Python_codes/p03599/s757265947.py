A, B, C, D, E, F = map(int, input().split())
max_a = int(3000 / (100 * A))
max_b = int(3000 / (100 * B))
max_c = int(3000 / C)
max_d = int(3000 / D)
max_dens = 0
max_sugar = 0
max_sugar_water = 0
for i in range(max_a + 1):
  water_A = 100 * A * i
  if water_A > F:
    break
  for j in range(max_b + 1):
    water = 100 * B * j + water_A
    if water > F:
      break
    max_solvable_sugar = E * water
    for s in range(max_c + 1):
      sugar_C = C * s
      if sugar_C * 100 > max_solvable_sugar:
        break
      for t in range(max_d + 1):
        sugar = D * t + sugar_C
        if sugar * 100 > max_solvable_sugar:
          break
        sugar_water = water + sugar
        if sugar_water > F or sugar_water == 0:
          break
        dens = 100 * sugar / sugar_water
        if dens >= max_dens:
          max_dens = dens
          max_sugar = sugar
          max_sugar_water = sugar_water
print("{} {}".format(max_sugar_water, max_sugar))