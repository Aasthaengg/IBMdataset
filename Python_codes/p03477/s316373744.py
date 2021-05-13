A, B, C, D = (int(x) for x in input().split())
if A + B < C + D:
  print('Right')
if A + B > C + D:
  print('Left')
if A + B == C + D:
  print('Balanced')
