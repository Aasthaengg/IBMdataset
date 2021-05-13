x = input().split()
if int(x[0]) >= 10:
  print(x[1])
else:
  r = int(x[1]) + 100*(10 - int(x[0]))
  print(r)