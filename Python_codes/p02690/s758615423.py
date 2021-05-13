x = int(input())
for i in range(-120,121):
  for j in range(-120, 121):
    if i ** 5 - j ** 5 == x:
      print(i,j)
      break
  if i ** 5 - j ** 5 == x:
    break