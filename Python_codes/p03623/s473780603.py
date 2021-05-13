base, shopA, shopB = map(int, input().split())
if abs(base - shopA) < abs(base - shopB):
  print("A")
else:
  print("B")