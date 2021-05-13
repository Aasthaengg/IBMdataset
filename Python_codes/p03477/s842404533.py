a, b, c, d = list(map(int, input().split()))

A = a + b
B = c + d
if A == B:
  print('Balanced')
elif A > B:
  print('Left')
elif A < B:
  print('Right')
