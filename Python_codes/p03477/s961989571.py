a,b,c,d = map(int, input().split())
res = a+b - (c+d)
if res > 0:
  print('Left')
elif res == 0:
  print('Balanced')
else:
  print('Right')