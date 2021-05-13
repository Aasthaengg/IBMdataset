x = str(input())
z = 0
t = 0
for xi in x:
  if xi == "S":
    z += 1
  if xi == "T":
    if z >= 1:
      z -= 1
    else:
      t += 1
print(t+z)