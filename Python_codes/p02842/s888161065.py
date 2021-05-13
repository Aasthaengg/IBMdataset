n = int(input())
if n%1.08==0:
  print(int(n//1.08))
else:
  x_init=n//1.08 + 1
  x_n = int(1.08*x_init)
  if x_n ==n:
    print(int(x_init))
  else:
    print(':(')