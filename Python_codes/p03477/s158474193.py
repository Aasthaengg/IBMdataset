a, b, c, d = (int(i) for i in input().split())

l = a+b
r = c+d
if l > r:
  print('Left')
elif r > l:
  print('Right')
else:
  print('Balanced')