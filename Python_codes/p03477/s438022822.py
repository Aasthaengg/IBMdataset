A, B, C, D = map(int, input().split())
a = A + B
c = C + D

if a > c:
  print("Left")
elif a < c:
  print("Right")
else:
  print("Balanced")