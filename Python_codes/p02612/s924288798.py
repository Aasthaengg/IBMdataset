price = int(input())

a = price % 1000
c = 1000 - a

if a == 0:
  print(0)
else:
  print(c)
