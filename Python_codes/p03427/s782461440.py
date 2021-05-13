n = input()
x = len(n)

if x == 1:
  print(int(n))
else:
  if int(n[0]) < int((int(n) + 1) / int("1"+"0"*(x-1))):
    print(int(n[0]) + 9 * (x - 1))
  else:
    print(int(n[0]) - 1 + 9 * (x - 1))