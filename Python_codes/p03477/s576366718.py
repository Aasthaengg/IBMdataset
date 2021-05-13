x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
left = a+b
right = c+d
if left > right:
  print('Left')
elif left < right:
  print('Right')
else:
  print('Balanced')