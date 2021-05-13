A,B,C,D = tuple(int(num) for num in input().split())

left = A + B
right = C + D

if right > left:
  print('Right')
elif right == left:
  print('Balanced')
else:
  print('Left')