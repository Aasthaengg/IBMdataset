x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)
#print("x =", x)
#print("a =", a)
#print("b =", b)

if x < a:
  xa = a - x
else:
  xa = x - a
  
if x < b:
  xb = b - x
else:
  xb = x - b

if xa > xb:
  print('B')
else:
  print('A')