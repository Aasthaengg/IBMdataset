def z(x):
  fives = 0
  for j in range(1, 60):
    bs = 2 * 5 ** j
    fives = fives + x // bs
  return fives
x = int(input())
print(z(x) if x % 2 == 0 else 0)