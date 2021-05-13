a = input()
b = a.split()
x = int(b[0])
y = int(b[1])
z = int(b[2])

if(x+y == z):
  print("Yes")
elif(x+z == y):
  print("Yes")
elif(y+z == x):
  print("Yes")
else:
  print("No")