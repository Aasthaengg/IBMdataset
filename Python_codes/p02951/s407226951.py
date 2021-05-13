A, B, C = map(int, input().split())
rem = A-B
if C >= rem:
  print(C-rem)
else:
  print("0")