A,B,C,D= (int(x) for x in input().split())
left = A+ B
right = C+D

if left == right:
  print('Balanced')
elif left  > right:
  print('Left')
elif left < right:
  print('Right')