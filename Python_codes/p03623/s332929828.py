getList = lambda: list(map(int, input().split()))
x,a,b = getList()
if abs(a - x) < abs(b - x):
  print("A")
else:
  print("B")