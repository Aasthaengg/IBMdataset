getList = lambda: list(map(int, input().split()))
a, b = getList()
if a <= b:
  print("unsafe")
else:
  print("safe")