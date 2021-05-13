x = int(input())
div,mod = divmod(x, 100)

if mod==0:
  print(1)
else:
  if div*5 >= mod:
    print(1)
  else:
    print(0)