A, B, C, D = map(int, input().split())
if A+B > C+D:
  print("Left")
if A+B == C+D:
  print("Balanced")
if A+B < C+D:
  print("Right")