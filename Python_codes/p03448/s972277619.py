a, b, c, x = int(input()), int(input()), int(input()), int(input())
count = 0
for i in range(a + 1):
  p = x - i * 500
  if p < 0 :
    continue
  elif p == 0:
    count += 1
    continue
  for j in range(b + 1):
    q = p - j * 100
    if q < 0 :
      continue
    elif q == 0:
      count += 1
      continue
    for k in range(c + 1):      
      if q - k * 50 == 0 :
        count += 1
      else:
        continue
      
print(count)