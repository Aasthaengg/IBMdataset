x = int(input())

num = 360

while True:
  if num % x == 0:
    print(num // x)
    break
  else:
    num += 360