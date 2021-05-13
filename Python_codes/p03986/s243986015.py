a = b = 0
for s in input():
  if s == 'S':
    a += 1
  else:
    if a == 0:
      b += 1
    else:
      a -= 1
print(a+b)