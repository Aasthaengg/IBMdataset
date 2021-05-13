a,b = [int(x) for x in input().split()]
if a > b:
  print(str(b) * a)
else:
  print(str(a) * b)