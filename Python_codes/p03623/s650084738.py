x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)
if x < a:
  dis_ax = a-x
else:
  dis_ax = x-a
if x < b:
  dis_bx = b-x
else:
  dis_bx = x-b
if dis_ax > dis_bx:
  print("B")
else:
  print("A")