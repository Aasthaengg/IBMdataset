l = map(int, raw_input().split())

if l[0]+l[1] > l[2]+l[3]:
  print('Left')
elif l[0]+l[1] == l[2]+l[3]:
  print('Balanced')
else:
  print('Right')