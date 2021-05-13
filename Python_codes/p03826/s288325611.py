x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
a_b = a*b
c_d = c*d
if a_b > c_d:
  print(a_b)
else:
  print(c_d)