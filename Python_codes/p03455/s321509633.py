
x = input().split()
a = x[0]
b = x[1]
c = int(a) * int(b)
d = c % 2
if d == 0:
  print('Even')
else:
  print('Odd')
