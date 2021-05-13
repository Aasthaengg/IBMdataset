A, B, C, D, E, F = map(int, input().split())

x = set()

for i in range(F):
  for j in range(F):
    water = 100 * A * i + 100 * B * j
    if F >=  water:
      x.add(water)
    else:
      break

sugar = water / 100 * E

y = set()

for i in range(F):
  for j in range(F):
    sugar = C * i + D * j
    if F >= sugar:
      y.add(sugar)
    else:
      break

x = list(x) # water
y = list(y) # sugar
percentage = 0
sugarWater = 0
ansSugar = 0

for i in range(len(x)):
  for j in range(len(y)):
    if x[i] + y[j] == 0:
      pass
    elif F >= x[i] + y[j]:
      if y[j] <= E * x[i] / 100:
        p = 100 * y[j] / ( x[i] + y[j] )
        if p >= percentage:
          percentage = p
          sugarWater = x[i] + y[j]
          ansSugar = y[j]

print(str(sugarWater) + " " + str(ansSugar))