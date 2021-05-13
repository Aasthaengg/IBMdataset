A, B, C, D = map(int, input().strip().split())

left = A+B
right = C+D
if left == right:
  print("Balanced")
else:
  print("Left" if left>right else "Right")
