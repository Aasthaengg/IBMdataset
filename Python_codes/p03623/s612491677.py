z = input().split()
x = int(z[0])
a = int(z[1])
b = int(z[2])
A = x - a
B = x - b
if A < 0:
  A = A*-1
if B < 0:
  B = B*-1
if A > B:
  print('B')
else:
  print('A')